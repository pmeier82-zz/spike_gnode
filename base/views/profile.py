# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

__author__ = "pmeier82"

User = get_user_model()


@login_required
def profile(request):
    return render(request, template_name="base/profile.html")


if __name__ == "__main__":
    pass
