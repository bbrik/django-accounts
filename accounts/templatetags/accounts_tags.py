# -*- coding: utf-8 -*-

from django.template import Library


register = Library()


@register.inclusion_tag('accounts/templatetags/field.html')
def bootstrap_field(field):
    return {
        'field': field,
    }