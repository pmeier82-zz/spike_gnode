# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BaseAppConfig(AppConfig):
    label = "base"
    name = "base"
    verbose_name = _("Base Application")

    def ready(self):
        # import all parts of the application that need to be exposed
        pass
