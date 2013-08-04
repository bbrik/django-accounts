# -*- coding: utf-8 -*-

from django.contrib.auth import views as auth_views


def login(request):
    return auth_views.login(request)
