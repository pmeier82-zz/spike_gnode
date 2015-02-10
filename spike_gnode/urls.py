# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.conf import settings
from rest_framework import routers

admin.autodiscover()

urlpatterns = patterns(
    "",
    url(r"^admin/", include(admin.site.urls)),
    url(r"^bad/$", lambda request: 1 / 0),
    url(r"^", include("base.urls")),
    url(r"^", include("djspikeval.urls")),
)

# bootstrap3 demos in the debug environment
if settings.DEBUG:
    import demo.urls

    demo_urls = patterns(
        "",
        url(r'^demo/', include(demo.urls, "demo", "demo"))
    )
    urlpatterns += demo_urls

if __name__ == "__main__":
    pass
