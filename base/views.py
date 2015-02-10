# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect

from sendfile import sendfile

__author__ = "pmeier82"

FileAsset = apps.get_registered_model(*settings.AUTH_USER_MODEL.split("."))
# User = apps.get_registered_model(*settings.AUTH_USER_MODEL.split("."))
User = get_user_model()


## other views

@login_required
def profile(request):
    return render(request, template_name="base/profile.html")


def serve_file(request, pk):
    """serve a datafile for download"""
    try:
        bf = FileAsset.objects.get(pk=pk)
        mine_type = bf.mine_type or None
        return sendfile(request, bf.file.path, attachment=True, attachment_filename=bf.name)
    except FileAsset.DoesNotExist:
        msg = "Error: could not find Datafile with id=`{}`".format(pk)
        messages.error(request, msg)
        # raise Http404(msg)


@login_required
def delete(request, pk):
    """delete datafile"""
    try:
        df = FileAsset.objects.get(pk=pk)
    except FileAsset.DoesNotExist:
        msg = "Error: could not find Datafile with id=`{}`".format(pk)
        messages.error(request, msg)
        raise Http404(msg)
    co = df.content_object
    assert co.has_access(request.user), "insufficient permissions"
    df.delete()
    messages.success(request, "Datafile {:s} deleted".format(df))
    return redirect(co)

## EOF
