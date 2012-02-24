from django.core.management.base import BaseCommand

from exercises.models import KhanExerciseTreeNode

def _generate_screenshots():
    from webkit2png import create_pngs

    exercises = KhanExerciseTreeNode.objects.exclude(live=False).values('url')
    urls = [exercise['url'] for exercise in exercises]
    options = {
        'dir': './static/images/exercise-screenshots/',
    }
    create_pngs(*urls, **options)

class Command(BaseCommand):
    help = 'Generates PNG screenshots of each live exercise in the database.'

    def handle(self, *args, **options):
        _generate_screenshots()
