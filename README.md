knetwork-exercises
==================
Imports exercises from the Khan Academy topic tree into a Django-ORM managed
database table stored with django-mptt.  To use, add `exercises` to
INSTALLED_APPS or use the included project configuration for testing purposes.

Dependencies
------------
This project has been built and tested on Python 2.7.1 and Django 1.3.1.

    $ pip install -r requirements.txt

Importing HOWTO
---------------
The test project configuration has dependencies on sqlite3.

    $ ./manage.py syncdb

The import can be executed by using the `import_exercises` management command:

    $ ./manage.py import_exercises

Then, to run the Django dev server:

    $ ./manage.py runserver

The sample menu navigation should now be accessible at http://localhost:8000

Thumbnail Generation
--------------------
Thumbnails for each Khan exercise page may be generated with the
`generate_thumbnails` management command (not implemented).
