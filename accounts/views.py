# -*- coding: utf-8 -*-

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.shortcuts import resolve_url


ACCOUNTS_BASE_TEMPLATE = getattr(settings, 'ACCOUNTS_BASE_TEMPLATE', 'base.html')
EXTRA_CONTEXT = {
    'accounts_base': ACCOUNTS_BASE_TEMPLATE,
}


def resolve_url_for_config(name):
    url = getattr(settings, name, None)
    if url is not None:
        return resolve_url(url)
    return None


LOGOUT_REDIRECT_URL = resolve_url_for_config('LOGOUT_REDIRECT_URL') or '/'


def login(request):
    return auth_views.login(request, extra_context=EXTRA_CONTEXT)


def logout(request):
    return auth_views.logout(request, extra_context=EXTRA_CONTEXT,
                             next_page=LOGOUT_REDIRECT_URL)

