django-remplacer
================

Easy search and replace in database fields via Django model introspection.


Install
-------
::
    pip install django-remplacer


Settings
--------
::
    INSTALLED_APPS = [
        ...,
        remplacer,
        ...,
    ]


Usage
-----
::
    python manage.py remplace TARGET REPLACEMENT


Help
----
::
    python manage.py remplace -h