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

Exercises Update
----------------
Instead of generating screenshots, now the exercises are loaded from the 
khan-exercises Github repository. The command to pull the latest updates is

		$ ./manage.py clone_khan_exercies

Test Server
-----------
To run the Django dev server:

    $ ./manage.py runserver

The sample menu navigation should now be accessible at http://localhost:8000
