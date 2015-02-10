# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from registration.backends.default.views import RegistrationView

from forms import CaptchaRegistrationForm

__author__ = "pmeier82"

urlpatterns = patterns(
    "base.views",
    # registration
    url(r"accounts/register/$",
        RegistrationView.as_view(form_class=CaptchaRegistrationForm),
        name="registration_register"),
    url(r'^accounts/', include("registration.backends.default.urls")),

    # base urls
    url(r"^$", TemplateView.as_view(template_name="base/home.html"), name="home"),
    url(r'^imprint$', TemplateView.as_view(template_name="base/imprint.html"), name="imprint"),
    url(r'^team$', TemplateView.as_view(template_name="base/team.html"), name="team"),
)

## EOF
