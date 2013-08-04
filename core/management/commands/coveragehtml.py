# -*- coding: utf-8 -*-

from subprocess import call
import errno

from unipath import Path

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


try:
    PROJECT_ROOT = Path(settings.PROJECT_ROOT)
except AttributeError:
    error_msg = "Define PROJECT_ROOT in settings"
    raise ImproperlyConfigured(error_msg)


INCLUDE_PATH = PROJECT_ROOT.child('*')


class Command(BaseCommand):
    help = 'Run test with coverage'

    def handle(self, *args, **options):
        PROJECT_ROOT.chdir()
        try:
            call('coverage html --include="%s" --omit="admin.py"' % INCLUDE_PATH, shell=True)
        except OSError as e:
            if e.errno == errno.ENOENT:
                error_msg = "coverage not found."
                raise ImproperlyConfigured(error_msg)
            else:
                raise
