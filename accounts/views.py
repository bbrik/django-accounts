# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.contrib import messages


ACCOUNTS_BASE_TEMPLATE = getattr(settings, 'ACCOUNTS_BASE_TEMPLATE', 'base.html')
EXTRA_CONTEXT = {
    'accounts_base': ACCOUNTS_BASE_TEMPLATE,
}


def resolve_url_for_config(name):
    url = getattr(settings, name, None)
    if url is not None:
        return resolve_url(url)
    return None


def is_redirect(response):
    return type(response) is HttpResponseRedirect


LOGOUT_REDIRECT_URL = resolve_url_for_config('LOGOUT_REDIRECT_URL') or '/'
PASSWORD_CHANGE_REDIRECT = resolve_url_for_config('PASSWORD_CHANGE_REDIRECT') or '/'


def login(request):
    return auth_views.login(request, extra_context=EXTRA_CONTEXT)


def logout(request):
    return auth_views.logout(request, extra_context=EXTRA_CONTEXT,
                             next_page=LOGOUT_REDIRECT_URL)


def password_change(request):
    response = auth_views.password_change(
        request,
        post_change_redirect=PASSWORD_CHANGE_REDIRECT,
        extra_context=EXTRA_CONTEXT,
    )
    if is_redirect(response):
        msg = _(u'Senha alterada com sucesso.')
        messages.success(request, msg)
    return response