import os

import Image, ImageChops

from django.conf import settings
from django.core.management.base import BaseCommand

from exercises.models import KhanExerciseTreeNode

def trim(im, bg=(255, 255, 255, 0)):
    bg = Image.new(im.mode, im.size, bg)
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    else:
        # found no content
        raise ValueError('cannot trim; image was empty')

def crop_screenshots():
    exercises = KhanExerciseTreeNode.objects.filter(live=True).exclude(url=None)
    exercise_files = [e.readable_filename for e in exercises]
    for filename in os.listdir(settings.KHAN_EXERCISE_SCREENSHOT_DIR):
        if not filename in exercise_files:
            continue

        # Load image and trim
        filename = os.path.join(settings.KHAN_EXERCISE_SCREENSHOT_DIR, filename)
        image = trim(Image.open(filename))

        # Save image
        filename, ext = os.path.splitext(filename)
        image.save(filename + '-trimmed.png', 'png')

class Command(BaseCommand):
    help = 'Crops out transparency from screenshots in settings.KHAN_EXERCISE_SCREENSHOT_DIR.'

    def handle(self, *args, **options):
        crop_screenshots()
