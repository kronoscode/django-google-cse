# -*- coding: utf-8 -*-
from django import template
register = template.Library()


@register.inclusion_tag('google_cse/searchform.html', takes_context=True)
def load_searchform(context):
    return {
        'q': context.get('q', '')
    }
