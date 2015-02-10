# -*- coding: utf-8 -*-

from django import template
import re

__author__ = "pmeier82"

register = template.Library()


@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return "active"
    return ""


if __name__ == "__main__":
    pass
