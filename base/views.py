# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from sendfile import sendfile

__author__ = "pmeier82"

Asset = apps.get_registered_model("base", "asset")
User = get_user_model()


@login_required
def profile(request):
    return render(request, template_name="base/profile.html")


def serve_asset(request, pk):
    """serve a asset for download"""

    try:
        bf = get_object_or_404(Asset, pk=pk)
        mine_type = bf.mine_type or None
        return sendfile(request, bf.file.path, attachment=True, attachment_filename=bf.name)
    except Asset.DoesNotExist:
        msg = "Error: could not find Datafile with id=`{}`".format(pk)
        messages.error(request, msg)
        raise


@login_required
def delete(request, pk):
    """delete datafile"""
    try:
        df = Asset.objects.get(pk=pk)
    except Asset.DoesNotExist:
        msg = "Error: could not find Datafile with id=`{}`".format(pk)
        messages.error(request, msg)
        raise Http404(msg)
    co = df.content_object
    assert co.has_access(request.user), "insufficient permissions"
    df.delete()
    messages.success(request, "Datafile {:s} deleted".format(df))
    return redirect(co)
