# -*- coding: utf-8 -*-

from .base import *

try:
    from .local import *
except ImportError, exc:
    exc.args = tuple(
        ['%s (did you rename settings/local-dist.py?)' % exc.args[0]])
    raise exc

__author__ = "pmeier82"
