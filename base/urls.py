# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from registration.backends.default.views import RegistrationView

from forms import CaptchaRegistrationForm

__author__ = "pmeier82"

patterns_asset = patterns(
    "base.views",
    url(r"^asset/(?P<pk>\d+)/$", "serve_asset", name="serve"),
    url(r"^serve_asset/(?P<pk>\d+)/$", "delete_asset", name="delete"),
)

urlpatterns = patterns(
    "base.views",

    # registration
    url(r"accounts/register/$",
        RegistrationView.as_view(form_class=CaptchaRegistrationForm),
        name="registration_register"),
    url(r'^accounts/', include("registration.backends.default.urls")),

    # base urls
    url(r"^$", TemplateView.as_view(template_name="base/home.html"), name="home"),
    url(r"^imprint$", TemplateView.as_view(template_name="base/imprint.html"), name="imprint"),
    url(r"^team$", TemplateView.as_view(template_name="base/team.html"), name="team"),

    # asset
    url(r"^asset/", include(patterns_asset, namespace="asset")),
)
