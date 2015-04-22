# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings

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
    # DEMO URLS
    try:
        import demo.urls

        demo_urls = patterns(
            "",
            url(r'^demo/', include(demo.urls, "demo", "demo"))
        )
        urlpatterns += demo_urls
    except:
        pass

    # MEDIA URLS
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if __name__ == "__main__":
    pass
