import os
from subprocess import call

from django.conf import settings
from django.core.management.base import BaseCommand

def _git_clone():
    os.chdir(os.getcwd() + "/static/khan-exercises")
    call(['git','checkout','khan-exercise.js'])
    call(['git','pull'])
    call(['cp','../khan-exercise.js', 'khan-exercise.js'])

class Command(BaseCommand):
    help = 'Gets the latest exercises from khan-exercises on Github'

    def handle(self, *args, **options):
        _git_clone()