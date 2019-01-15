#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron

from django import template
from django.utils.safestring import mark_safe



register = template.Library()  # register的名字是固定的,不可改变


@register.filter
def coustom_filter(x, y):
    return x * y

@register.simple_tag
def coustom_simple(x, y, z):

    return x+y+z