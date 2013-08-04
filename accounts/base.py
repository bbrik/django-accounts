# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect
from django.contrib import messages


def resolve_url_for_config(name):
    url = getattr(settings, name, None)
    if url is not None:
        return resolve_url(url)
    return None


def msg_success_redirect(msg):
    """
    Decorator para msg de success se a resposta da view for redirect.

    """
    def decorator(view_func):
        def wrapped(request, *args, **kwargs):
            response = view_func(request, *args, **kwargs)
            if type(response) is HttpResponseRedirect:
                messages.success(request, msg)
            return response
        return wrapped
    return decorator

