# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    url(
        regex=r'^login/$',
        view=views.login,
        name='login'
    ),
)
