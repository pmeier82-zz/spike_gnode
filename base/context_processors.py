# -*- coding: utf-8 -*-

from django.apps import apps

__author__ = "pmeier82"


def base(request):
    Site = apps.get_registered_model("sites", "site")
    obj = Site.objects.get_current()
    return {
        u"SITE_ID": obj.id,
        u"SITE_NAME": obj.name,
    }


if __name__ == "__main__":
    pass
