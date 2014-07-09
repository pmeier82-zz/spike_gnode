""" Views for the base application """

from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView


# def home(request):
#     """ Default view for the root """
#     return render(request, 'base/home.html')


def home(request):
    """ Default view for the root """
    messages.info(request, 'EST TEST TEST T')
    return render(request, 'base/home.html')


@login_required
def profile(request):
    return render(request, template_name='base/profile.html')
