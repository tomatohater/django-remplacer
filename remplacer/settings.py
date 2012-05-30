from django.conf import settings

#
# REMPLACER_IGNORE_APPS specifies which apps should be skipped. Nothing will
# be replaced in these apps. Defaults to commonly ignores apps.
#
REMPLACER_IGNORE_APPS = getattr(settings, 'REMPLACER_IGNORE_APPS',
    ['contenttypes', 'auth', 'sites', 'sessions', 'admin', 'south', ])