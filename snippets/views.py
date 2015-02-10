## -*- coding: utf-8 -*-

from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from rest_framework import viewsets
from sendfile import sendfile
from djdatafile.models import Datafile


def download(request, pk):
    """serve a datafile for download"""
    try:
        df = Datafile.objects.get(pk=pk)
        return sendfile(request, df.file.path, attachment=True, attachment_filename=df.name)
    except Datafile.DoesNotExist:
        msg = "Error: could not find Datafile with id=`{}`".format(pk)
        messages.error(request, msg)
        raise Http404(msg)


@login_required
def delete(request, pk):
    """delete datafile"""
    try:
        df = Datafile.objects.get(pk=pk)
    except Datafile.DoesNotExist:
        msg = "Error: could not find Datafile with id=`{}`".format(pk)
        messages.error(request, msg)
        raise Http404(msg)
    co = df.content_object
    assert co.has_access(request.user), "insufficient permissions"
    df.delete()
    messages.success(request, "Datafile {:s} deleted".format(df))
    return redirect(co)

## MAIN

if __name__ == "__main__":
    pass

## EOF
