# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    url(
        regex=r'^login/$',
        view=views.login,
        name='login'
    ),
    url(
        regex=r'^logout/$',
        view=views.logout,
        name='logout'
    ),
    url(
        regex=r'^password-change/$',
        view=views.password_change,
        name='password_change'
    ),
    url(
        regex=r'^password-reset/$',
        view=views.password_reset,
        name='password_reset'
    ),
    url(
        regex=r'^password-reset-confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view=views.password_reset_confirm,
        name='password_reset_confirm'
    ),
)
