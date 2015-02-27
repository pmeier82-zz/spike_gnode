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
        asset = get_object_or_404(Asset, pk=pk)
        return sendfile(request, asset.data.path, attachment=True, attachment_filename=asset.data.name)
    except Asset.DoesNotExist:
        msg = "Error: could not find Datafile with id=`{}`".format(pk)
        messages.error(request, msg)
        raise


@login_required
def delete_asset(request, pk):
    """delete datafile"""
    try:
        asset = get_object_or_404(Asset, pk=pk)
    except Asset.DoesNotExist:
        msg = "Error: could not find Datafile with id=`{}`".format(pk)
        messages.error(request, msg)
        raise Http404(msg)
    co = asset.content_object
    assert co.has_access(request.user), "insufficient permissions"
    asset.delete()
    messages.success(request, "Datafile {:s} deleted".format(asset))
    return redirect(co)


if __name__ == "__main__":
    pass
