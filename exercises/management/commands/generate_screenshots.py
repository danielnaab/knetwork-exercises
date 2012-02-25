from django.core.management.base import BaseCommand
from django.conf import settings

from exercises.models import KhanExerciseTreeNode

POST_LOAD_JS = """
    $(document).ready(function() {
        $("header, footer, #answer_area_wrap, #warning-bar, #extras, .exercise-badge").hide();
    });
"""

def _generate_screenshots():
    from webkit2png import create_pngs

    exercises = KhanExerciseTreeNode.objects.filter(live=True)
    urls = [e.url for e in exercises if e.get_descendant_count() == 0]
    options = {
        'dir': settings.KHAN_EXERCISE_SCREENSHOT_DIR,
        'js': POST_LOAD_JS
    }
    create_pngs(*urls, **options)

class Command(BaseCommand):
    help = 'Generates PNG screenshots of each live exercise in the database.'

    def handle(self, *args, **options):
        _generate_screenshots()
