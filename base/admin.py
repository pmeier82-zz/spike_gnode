# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from base.models import Profile, Asset

__author__ = "pmeier82"


class ProfileAdmin(admin.ModelAdmin):
    pass


class AssetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Asset, AssetAdmin)

if __name__ == "__main__":
    pass
