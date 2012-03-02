from subprocess import call

from django.conf import settings
from django.core.management.base import BaseCommand

from exercises.models import KhanExerciseTreeNode

POST_LOAD_JS = """
    $(document).ready(function() {
        $('header, footer, #answer_area_wrap, #warning-bar, #extras, .exercise-badge').hide();
        $('*').css('background', 'transparent');
    });
"""

def _generate_screenshots():
    exercises = KhanExerciseTreeNode.objects.filter(live=True).exclude(url=None)
    urls = [e.url for e in exercises if '#' not in e.url]

    # This should work fine, but there's a little issue with the webkit2png
    # with large lists of urls.  So we'll call the process instead, on 5 urls
    # at a time.
    #options = {
    #    'dir': settings.KHAN_EXERCISE_SCREENSHOT_DIR,
    #    'js': POST_LOAD_JS,
    #    'transparent': True,
    #    'fullsize': True,
    #    'delay': 2
    #}
    #from webkit2png import create_pngs
    #create_pngs(*urls, **options)

    options = [
        '--dir', settings.KHAN_EXERCISE_SCREENSHOT_DIR,
        '--js', POST_LOAD_JS,
        '--transparent',
        '--fullsize',
        '--delay', '2'
    ]
    for url in urls:
        args = ['webkit2png'] + [url] + options
        call(args)

class Command(BaseCommand):
    help = 'Generates PNG screenshots of each live exercise in the database.'

    def handle(self, *args, **options):
        _generate_screenshots()
