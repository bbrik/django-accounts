# -*- coding: utf-8 -*-

from django.contrib.auth import forms as auth_forms


class Bootstrap3FormMixin(object):
    def __init__(self, *args, **kwargs):
        super(Bootstrap3FormMixin, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class AuthenticationForm(Bootstrap3FormMixin, auth_forms.AuthenticationForm):
    pass


class PasswordChangeForm(Bootstrap3FormMixin, auth_forms.PasswordChangeForm):
    pass


class PasswordResetForm(Bootstrap3FormMixin, auth_forms.PasswordResetForm):
    pass


class SetPasswordForm(Bootstrap3FormMixin, auth_forms.SetPasswordForm):
    pass
