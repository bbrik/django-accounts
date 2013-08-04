# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect


def resolve_url_for_config(name):
    url = getattr(settings, name, None)
    if url is not None:
        return resolve_url(url)
    return None


def is_redirect(response):
    return type(response) is HttpResponseRedirect
