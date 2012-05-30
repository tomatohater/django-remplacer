django-remplacer
================

Easy search and replace in database fields via Django model introspection.


Install
-------

Install with pip::

    $ pip install django-remplacer


Settings
--------

Include `remplacer` in your INSTALLED_APPS::

    INSTALLED_APPS = [
        ...,
        remplacer,
        ...,
    ]


Usage
-----

Run the management command::

    $ python manage.py remplace TARGET REPLACEMENT [options]


Get help::

    $ python manage.py remplace -h