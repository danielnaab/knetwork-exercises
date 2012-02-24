from urllib2 import urlopen

from django.core.management.base import BaseCommand
from django.utils import simplejson

from exercises.models import KhanExerciseTreeNode

API_URL = 'http://www.khanacademy.org/api/v1/topictree'

def _import_tree(tree_dict):
    if tree_dict['kind'] == 'Topic':
        khan_id = tree_dict['id']
        display_name = tree_dict['title']
        live = True
        url = tree_dict['ka_url']
    elif tree_dict['kind'] == 'Exercise':
        khan_id = tree_dict['name']
        display_name = tree_dict['display_name']
        live = tree_dict['live']
        url = tree_dict['ka_url']
    else:
        return None

    node, created = KhanExerciseTreeNode.objects.get_or_create(khan_id=khan_id)
    node.display_name = display_name
    node.live = live
    node.url = url
    node.save()

    if tree_dict.has_key('children'):
        for item in tree_dict['children']:
            child = _import_tree(item)
            if child:
                child.move_to(node)

    return node

def _do_import():
    response = urlopen(API_URL).read()
    _import_tree(simplejson.loads(response))

class Command(BaseCommand):
    help = 'Populates the database with latest Khan exercises (via API).'

    def handle(self, *args, **options):
        _do_import()
