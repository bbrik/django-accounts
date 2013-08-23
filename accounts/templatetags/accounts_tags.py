# -*- coding: utf-8 -*-

from django.template import Library, loader, Context

from ..base import get_full_template_name


register = Library()


@register.simple_tag()
def bootstrap_field(field):
    template_name = get_full_template_name('templatetags/field.html')
    template = loader.get_template(template_name)
    context = Context({
        'field': field
    })
    return template.render(context)


@register.simple_tag()
def bootstrap_non_field_errors(form):
    template_name = get_full_template_name('templatetags/non_field_errors.html')
    template = loader.get_template(template_name)
    context = Context({
        'form': form,
    })
    return template.render(context)