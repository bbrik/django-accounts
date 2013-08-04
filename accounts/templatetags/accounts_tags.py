# -*- coding: utf-8 -*-

from django.template import Library


register = Library()


@register.inclusion_tag('accounts/templatetags/bootstrap_field.html')
def bootstrap_field(field):
    return {
        'field': field,
    }


@register.inclusion_tag('accounts/templatetags/bootstrap_non_field_errors.html')
def bootstrap_non_field_errors(form):
    return {
        'form': form,
    }