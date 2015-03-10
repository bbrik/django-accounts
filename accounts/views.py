# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm, 
    PasswordResetForm, 
    SetPasswordForm,
)

from .base import (
    msg_success_redirect, 
    ACCOUNTS_BASE_TEMPLATE, 
    LOGOUT_REDIRECT_URL,
    PASSWORD_CHANGE_REDIRECT_URL,
    PASSWORD_RESET_REDIRECT_URL, 
    get_full_template_name
)


EXTRA_CONTEXT = {
    'accounts_base': ACCOUNTS_BASE_TEMPLATE,
}


MESSAGES = {
    'password_change': _(u'Senha alterada com sucesso.'),
    'password_reset': _(u'Um email foi enviado para sua conta '
                        u'com instruções de como recuperar sua senha.'),
    'password_reset_confirm': _(u'Senha redefinida com sucesso.'),
}


def login(request):
    return auth_views.login(
        request,
        extra_context=EXTRA_CONTEXT,
        authentication_form=AuthenticationForm,
        template_name=get_full_template_name('login.html')
    )


def logout(request):
    return auth_views.logout(
        request,
        extra_context=EXTRA_CONTEXT,
        next_page=LOGOUT_REDIRECT_URL
    )


@msg_success_redirect(PASSWORD_CHANGE_REDIRECT_URL, MESSAGES['password_change'])
def password_change(request):
    return auth_views.password_change(
        request,
        post_change_redirect=PASSWORD_CHANGE_REDIRECT_URL,
        extra_context=EXTRA_CONTEXT,
        password_change_form=PasswordChangeForm,
        template_name=get_full_template_name('password_change_form.html')
    )


@msg_success_redirect(PASSWORD_RESET_REDIRECT_URL, MESSAGES['password_reset'])
def password_reset(request):
    return auth_views.password_reset(
        request,
        post_reset_redirect=PASSWORD_RESET_REDIRECT_URL,
        extra_context=EXTRA_CONTEXT,
        password_reset_form=PasswordResetForm,
        template_name=get_full_template_name('password_reset_form.html')
    )


@msg_success_redirect(PASSWORD_RESET_REDIRECT_URL, MESSAGES['password_reset_confirm'])
def password_reset_confirm(request, uidb64, token):
    return auth_views.password_reset_confirm(
        request,
        uidb64=uidb64,
        token=token,
        post_reset_redirect=PASSWORD_RESET_REDIRECT_URL,
        extra_context=EXTRA_CONTEXT,
        set_password_form=SetPasswordForm,
        template_name=get_full_template_name('password_reset_confirm.html')
    )

