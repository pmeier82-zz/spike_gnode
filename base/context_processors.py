# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.apps import apps

__author__ = "pmeier82"


def base(request):
    Site = apps.get_model("sites", "site")
    obj = Site.objects.get_current()
    return {
        u"SITE_ID": obj.id,
        u"SITE_NAME": obj.name,
    }


if __name__ == "__main__":
    pass
