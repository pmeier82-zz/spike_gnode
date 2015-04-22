# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from captcha.fields import ReCaptchaField
from registration.forms import RegistrationForm
from django import forms
from django.apps import apps
from djspikeval.forms.util import form_with_captcha

__all__ = ["form_with_captcha", "CaptchaRegistrationForm", "AssetForm"]
__author__ = "pmeier82"

Asset = apps.get_model("base", "asset")


@form_with_captcha
class CaptchaRegistrationForm(RegistrationForm):
    pass


@form_with_captcha
class AssetForm(forms.ModelForm):
    """`Asset` model form"""

    # meta
    class Meta:
        model = Asset
        fields = ("name", "data")

    # constructor
    def __init__(self, *args, **kwargs):
        kind = kwargs.pop("kind", "default")
        obj = kwargs.pop("obj", None)
        if obj is None:
            raise ValueError("no related object passed!")
        super(AssetForm, self).__init__(*args, **kwargs)
        if self.instance.id is None:
            self.instance.kind = kind
            self.instance.content_object = obj

    # interface
    def save(self, *args, **kwargs):
        if self.instance.data is not None:
            self.instance.data_orig_name = self.instance.data.name
        return super(AssetForm, self).save(*args, **kwargs)


if __name__ == "__main__":
    pass
