# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import template
import re

__all__ = ["active"]
__author__ = "pmeier82"

register = template.Library()


# BASE

@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return u"active"
    return u""


# FONT AWESOME

@register.simple_tag
def fa_text(text, icons, link=None, color=None, strong=False, title=None):
    try:
        text = text.strip()
    except:
        text = "{}".format(text)
    icons = " ".join(["fa-" + icon for icon in icons.split(",")])
    ttl = "" if title is None else " title=\"{}\"".format(title or text)
    col = "" if color is None else " style=\"color: {};\"".format(color)
    rval = "<nobr><i class=\"fa {icons}\"></i> {a}{c}{s}{text}{s_}{c_}{a_}</nobr>"
    return rval.format(
        icons=icons,
        a="<a href=\"{}\">".format(link) if link is not None else "",
        c="<span{}{}>".format(col, ttl),
        s="<strong>" if strong is True else "",
        text=text,
        s_="</strong>" if strong is True else "",
        c_="</span>",
        a_="</a>" if link is not None else ""
    )


if __name__ == "__main__":
    pass
