"""urlconf for the base application"""

from django.conf.urls import include, patterns, url


urlpatterns = patterns(
    'base.views',
    url(r'^$', 'home', name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
