# -*- coding: utf-8 -*-

from django.contrib import admin
from base.models import Profile, Asset

__author__ = "pmeier82"


class BaseProfileAdmin(admin.ModelAdmin):
    pass


class BaseFileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, BaseProfileAdmin)
admin.site.register(Asset, BaseFileAdmin)

if __name__ == "__main__":
    pass
