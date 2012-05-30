from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from remplacer import settings


class Command(BaseCommand):
    args = 'target replacement'
    option_list = BaseCommand.option_list + (
        make_option('--dry-run', '-d', dest='dryrun',
            help='Dry-run only. Don\'t really change anything.', default=False, action='store_true',),
         make_option('--noinput', '-n', dest='noinput',
            help='Don\'t ask for confirmation. Just do it', default=False, action='store_true',),
    )
    help = 'Search and replace in database fields via Django model introspection.'

    def handle(self, findstr, replacestr, **options):
        from django.db import models
        models = models.get_models()

        verbosity = int(options['verbosity'])

        if not options['noinput']:
            self.stdout.write('This will replace all instances of String A with String B...\n');
            self.stdout.write('  A: %s\n' % findstr);
            self.stdout.write('  B: %s\n' % replacestr);
            confirmation = raw_input('Are you sure? [Y, n]: ')
            if confirmation not in ['', 'y', 'Y']:
                exit()

        counter = 0
        for model in models:
            if model._meta.app_label not in settings.REMPLACER_IGNORE_APPS:
                if verbosity >= 2:
                   self.stdout.write('Checking %s\n' % model)
                objects = model.objects.all()
                for object in objects:
                    for field in object._meta.fields:
                        field_value = getattr(object, field.name, None)
                        if isinstance(field_value, basestring):
                            try:
                                if field_value.find(findstr) > -1:
                                    if verbosity >= 2:
                                        print 'Found', field.name, object.pk, getattr(object, field.name, '')
                                    if not options['dryrun']:
                                        setattr(object, field.name, field_value.replace(findstr, replacestr))
                                        object.save()
                                        if verbosity >= 2:
                                            self.stdout.write('Replaced!\n')
                                    counter += 1
                            except AttributeError:
                                pass
        if verbosity >= 1:
            self.stdout.write('Done! Replaced %s instances.\n' % counter)
            if options['dryrun']:
                self.stdout.write('Just kidding. Didn\'t really do anything (--dry-run was enabled).\n')
