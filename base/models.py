"""models for the base application"""

from django.db import models
from registration.signals import user_registered

## USER PROFILE

class SpikeGnodeUserProfile(models.Model):
    user = models.ForeignKey("User", unique=True)
    is_human = models.BooleanField()

    def __unicode__(self):
        return self.user

## SIGNALS

def user_registered_callback(sender, user, request, **kwargs):
    profile = SpikeGnodeUserProfile(user=user)
    profile.is_human = bool(request.POST["is_human"])
    profile.save()


user_registered.connect(user_registered_callback)
