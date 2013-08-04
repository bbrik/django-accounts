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
)
