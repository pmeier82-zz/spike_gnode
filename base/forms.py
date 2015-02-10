# -*- coding: utf-8 -*-

from captcha.fields import ReCaptchaField
from registration.forms import RegistrationForm

__author__ = "pmeier82"
__all__ = ["CaptchaRegistrationForm"]


class CaptchaRegistrationForm(RegistrationForm):
    captcha = ReCaptchaField()


if __name__ == "__main__":
    pass
