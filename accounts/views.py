# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import views as auth_views
from django.conf import settings

from .base import resolve_url_for_config, msg_success_redirect


ACCOUNTS_BASE_TEMPLATE = getattr(settings, 'ACCOUNTS_BASE_TEMPLATE', 'base.html')
EXTRA_CONTEXT = {
    'accounts_base': ACCOUNTS_BASE_TEMPLATE,
}
LOGOUT_REDIRECT_URL = resolve_url_for_config('LOGOUT_REDIRECT_URL') or '/'
PASSWORD_CHANGE_REDIRECT = resolve_url_for_config('PASSWORD_CHANGE_REDIRECT') or '/'
PASSWORD_RESET_REDIRECT = resolve_url_for_config('PASSWORD_RESET_REDIRECT') or '/'


def login(request):
    return auth_views.login(request, extra_context=EXTRA_CONTEXT)


def logout(request):
    return auth_views.logout(request, extra_context=EXTRA_CONTEXT,
                             next_page=LOGOUT_REDIRECT_URL)


@msg_success_redirect(PASSWORD_CHANGE_REDIRECT, _(u'Senha alterada com sucesso.'))
def password_change(request):
    return auth_views.password_change(
        request,
        post_change_redirect=PASSWORD_CHANGE_REDIRECT,
        extra_context=EXTRA_CONTEXT,
    )


@msg_success_redirect(PASSWORD_RESET_REDIRECT,
                      _(u'Um email foi enviado para sua conta '
                        u'com instruções de como recuperar sua senha.'))
def password_reset(request):
    return auth_views.password_reset(
        request,
        post_reset_redirect=PASSWORD_RESET_REDIRECT,
        extra_context=EXTRA_CONTEXT,
    )


@msg_success_redirect(PASSWORD_RESET_REDIRECT, _(u'Senha redefinida com sucesso.'))
def password_reset_confirm(request, uidb36, token):
    return auth_views.password_reset_confirm(
        request,
        uidb36=uidb36,
        token=token,
        post_reset_redirect=PASSWORD_RESET_REDIRECT,
        extra_context=EXTRA_CONTEXT,
    )

