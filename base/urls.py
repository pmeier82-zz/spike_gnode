# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from registration.backends.default.views import RegistrationView

from .views import AssetCreate, AssetDelete, AssetServe
from .forms import CaptchaRegistrationForm

__author__ = "pmeier82"

patterns_asset = patterns(
    "",
    url(r"^create/(?P<kind>\w+)/(?P<model>\w+)/(?P<pk>\d+)/$", AssetCreate.as_view(), name="create"),
    url(r"^(?P<pk>\d+)/delete/$", AssetDelete.as_view(), name="delete"),
    url(r"^(?P<pk>\d+)/serve/$", AssetServe.as_view(), name="serve"),
)

urlpatterns = patterns(
    "",

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

if __name__ == "__main__":
    pass
