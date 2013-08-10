# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect
from django.contrib import messages


def resolve_url_for_config(name, default=None):
    url = getattr(settings, name, None)
    if url is not None:
        return resolve_url(url)
    return default


ACCOUNTS_BASE_TEMPLATE = getattr(settings, 'ACCOUNTS_BASE_TEMPLATE', 'base.html')
LOGOUT_REDIRECT_URL = resolve_url_for_config('LOGOUT_REDIRECT_URL', '/')
PASSWORD_CHANGE_REDIRECT_URL = resolve_url_for_config('PASSWORD_CHANGE_REDIRECT_URL', '/')
PASSWORD_RESET_REDIRECT_URL = resolve_url_for_config('PASSWORD_RESET_REDIRECT_URL', '/')


def msg_success_redirect(success_url, msg):
    """
    Decorator para func views.
    Gera msg de success se a resposta da view for redirect para url especificada.

    """
    def decorator(view_func):
        def wrapped(request, *args, **kwargs):
            response = view_func(request, *args, **kwargs)
            if type(response) is HttpResponseRedirect and \
                            response['location'] == success_url:
                messages.success(request, msg)
            return response
        return wrapped
    return decorator

