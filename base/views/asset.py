# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DeleteView, CreateView
from sendfile import sendfile
from ..forms import AssetForm

__all__ = ["AssetBaseView", "AssetCreate", "AssetDelete", "AssetServe"]
__author__ = "pmeier82"

Asset = apps.get_registered_model("base", "asset")


class AssetBaseView(object):
    model = Asset


class AssetCreate(AssetBaseView, SuccessMessageMixin, CreateView):
    template_name = "base/asset/create.html"
    form_class = AssetForm
    success_message = "Attachment created!"

    def get_form_kwargs(self):
        kwargs = super(AssetCreate, self).get_form_kwargs()
        kwargs["kind"] = self.kwargs.get("kind")
        kwargs["obj"] = self.get_related_object()
        return kwargs

    def get_success_url(self):
        return self.object.content_object.get_absolute_url()

    def get_related_object(self):
        ct = ContentType.objects.get(
            app_label="djspikeval",
            model=self.kwargs.get("model").lower())
        return ct.get_object_for_this_type(pk=self.kwargs.get("pk"))


class AssetDelete(AssetBaseView, SuccessMessageMixin, DeleteView):
    template_name = "base/asset/delete.html"
    success_message = "Attachment deleted!"

    def get_success_url(self):
        return self.object.content_object.get_absolute_url()

    def get_related_object(self):
        ct = ContentType.objects.get(
            app_label="djspikeval",
            model=self.kwargs.get("model").lower())
        return ct.get_object_for_this_type(pk=self.kwargs.get("pk"))


class AssetServe(AssetBaseView, View):
    """Asset serving"""

    def get(self, request, *args, **kwargs):
        try:
            asset = get_object_or_404(Asset, pk=self.kwargs.get("pk"))
            return sendfile(
                request,
                asset.data.path,
                attachment=True,
                attachment_filename=asset.data_orig_name)
        except Asset.DoesNotExist:
            msg = "Error: could not find Datafile with id=`{}`".format(pk)
            messages.error(request, msg)
            raise


if __name__ == "__main__":
    pass
