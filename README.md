knetwork-exercises
==================
Imports exercises from the Khan Academy topic tree into a Django-ORM managed
database table stored with django-mptt.  To use, add `exercises` to
INSTALLED_APPS or use the included project configuration for testing purposes.

The app provides a view which renders the exercise tree as a menu, where each
exercise has a PNG preview.

Dependencies
------------
This project has been built and tested on Python 2.7.1 and Django 1.3.1.
It requires pyobjc (OS X) for screenshot generation via a library version of
the webkit2png tool (https://github.com/danielnaab/webkit2png).  To trim the
images, the Python Imaging Library is required.

    $ pip install -r requirements.txt

Importing HOWTO
---------------
The test project configuration has dependencies on sqlite3.

    $ ./manage.py syncdb

The import can be executed by using the `import_exercises` management command:

    $ ./manage.py import_exercises

Thumbnail Generation
--------------------
Thumbnails for each Khan exercise page may be generated with the
`generate_screenshots` management command.  OS X and pyobjc are required.

    $ ./manage.py generate_screenshots

The screenshots are placed in the app's static/images/exercise-screenshots
directory.

There is a separate command available to trim the images to a minimum size:

    $ ./manage.py crop_screenshots

Test Server
-----------
To run the Django dev server:

    $ ./manage.py runserver

The sample menu navigation should now be accessible at http://localhost:8000
