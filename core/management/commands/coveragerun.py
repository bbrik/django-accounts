# -*- coding: utf-8 -*-

from subprocess import call
import errno

from unipath import Path

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


class Command(BaseCommand):
    help = 'Run test with coverage'

    def handle(self, *args, **options):
        try:
            call('coverage run manage.py test --settings=accounts_proj.settings.test', shell=True)
        except OSError as e:
            if e.errno == errno.ENOENT:
                error_msg = "coverage not found."
                raise ImproperlyConfigured(error_msg)
            else:
                raise
