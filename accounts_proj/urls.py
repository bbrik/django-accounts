# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^', include('home.urls', namespace='home')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
)
