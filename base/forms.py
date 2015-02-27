# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from captcha.fields import ReCaptchaField
from registration.forms import RegistrationForm
from django import forms
from django.apps import apps

__all__ = ["form_with_captcha", "CaptchaRegistrationForm", "AssetForm"]
__author__ = "pmeier82"

Asset = apps.get_registered_model("base", "asset")


def form_with_captcha(orig_form):
    if hasattr(orig_form, "recaptcha"):
        raise ValueError("form already has a field with name \"recaptcha\"!")
    orig_form.__orig__init__ = orig_form.__init__

    def new_init(self, *args, **kwargs):
        self.__orig__init__(*args, **kwargs)
        self.fields["recaptcha"] = self.captcha

    orig_form.__init__ = new_init
    orig_form.captcha = ReCaptchaField()
    return orig_form


class CaptchaRegistrationForm(RegistrationForm):
    captcha = ReCaptchaField()


# @form_with_captcha
class AssetForm(forms.ModelForm):
    """`Asset` model form"""

    # meta
    class Meta:
        model = Asset
        fields = ("name", "data")

    # constructor
    def __init__(self, *args, **kwargs):
        self.kind = kwargs.pop("kind", "default")
        self.obj = kwargs.pop("obj", None)
        if self.obj is None:
            raise ValueError("no related object passed!")
        super(AssetForm, self).__init__(*args, **kwargs)

    # interface
    def save(self, *args, **kwargs):
        self.instance.kind = self.kind
        self.instance.content_object = self.obj
        self.instance.data_orig_name = self.instance.data.name
        return super(AssetForm, self).save(*args, **kwargs)


if __name__ == "__main__":
    pass
