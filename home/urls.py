# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=views.HomeView.as_view(),
        name='home'
    ),
)
