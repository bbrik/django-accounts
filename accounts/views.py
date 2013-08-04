# -*- coding: utf-8 -*-

from django.contrib.auth import views as auth_views
from django.conf import settings


ACCOUNTS_BASE_TEMPLATE = getattr(settings, 'ACCOUNTS_BASE_TEMPLATE', 'base.html')


def login(request):
    extra_context = {
        'accounts_base': ACCOUNTS_BASE_TEMPLATE,
    }
    return auth_views.login(request, extra_context=extra_context)
