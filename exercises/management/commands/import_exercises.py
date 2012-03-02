from urllib2 import urlopen

from django.core.management.base import BaseCommand
from django.utils import simplejson

from exercises.models import KhanExerciseTreeNode

API_URL = 'http://www.khanacademy.org/api/v1/topictree'
API_URL_EXERCISES = 'http://www.khanacademy.org/api/v1/exercises'

def _import_tree(tree_dict):
    if tree_dict['kind'] == 'Topic':
        khan_id = tree_dict['id']
        display_name = tree_dict['title']
        live = True
        url = None # make None because it's not an exercise
        num_exercises = 0
        is_topic = True
    elif tree_dict['kind'] == 'Exercise':
        khan_id = tree_dict['name']
        display_name = tree_dict['display_name']
        live = tree_dict['live']
        url = tree_dict['ka_url']
        is_topic = False
        num_exercises = 1
    else:
        return None, 0

    node, created = KhanExerciseTreeNode.tree.get_or_create(khan_id=khan_id)
    node.display_name = display_name
    node.live = live
    node.url = url
    node.is_topic = is_topic
    node.save()

    if tree_dict.has_key('children'):
        for item in tree_dict['children']:
            child, _num_exercises = _import_tree(item)
            if _num_exercises > 0:
                num_exercises += _num_exercises
                try:
                    parent, created = KhanExerciseTreeNode.tree.get_or_create(khan_id=khan_id)
                    child.move_to(parent)
                except Exception, e:
				    print child.url
				    print node.display_name
            elif child:
                # if there are no exercises on this category, remove from
                # database.
                child.delete()

    return node, num_exercises

def _import_old_list(exercises):
    uncategorized, created = KhanExerciseTreeNode.tree.get_or_create(
        khan_id='uncategorized',
        display_name='Uncategorized Exercises',
        live=True,
        url=None,
        is_topic=True
    )
    uncategorized.move_to(KhanExerciseTreeNode.tree.get(khan_id='math'))
    for exercise in exercises:
        print exercise['display_name']
        try:
            node = KhanExerciseTreeNode.tree.get(
                khan_id=exercise['name'])
            node.live = exercise['live']
            node.url = exercise['ka_url']
            node.display_name = exercise['display_name']
            node.is_topic = False
            node.save()
        except KhanExerciseTreeNode.DoesNotExist:
            node = KhanExerciseTreeNode(
                khan_id=exercise['name'],
                display_name=exercise['display_name'],
                live=exercise['live'],
                url=exercise['ka_url'],
                is_topic=False
            )
            node.save()
            node.move_to(uncategorized)

def _do_import():
    # Import the topic tree
    response = urlopen(API_URL).read()
    _import_tree(simplejson.loads(response))

    # Import the old exercise list
    response = urlopen(API_URL_EXERCISES).read()
    _import_old_list(simplejson.loads(response))

    KhanExerciseTreeNode.tree.rebuild()

class Command(BaseCommand):
    help = 'Populates the database with latest Khan exercises (via API).'

    def handle(self, *args, **options):
        _do_import()
