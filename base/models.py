# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from model_utils.models import TimeStampedModel
from registration.signals import user_registered

__author__ = "pmeier82"


# PROFILE

class Profile(models.Model):
    """user profile model"""

    class Meta:
        app_label = "base"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        unique=True)
    title = models.CharField(
        max_length=255,
        default="",
    )
    affiliation = models.CharField(
        max_length=255,
        default="",
    )
    research_area = models.TextField(
        default=""
    )
    # TODO: build a meaningful profile

    # special
    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return unicode(self.__str__())


def user_registered_callback(sender, instance, request, **kwargs):
    profile = Profile.objects.get_or_create(user=instance)
    profile.title = request.POST.get("title", "")
    profile.save()


user_registered.connect(user_registered_callback)

# ASSET

def UPLOAD_TO_HANDLER(obj, fname):
    folder = getattr(obj, "kind", "default")
    return "{}/{}".format(folder, fname)


class Asset(TimeStampedModel):
    """generic file asset model"""

    class Meta:
        app_label = "base"

    UPLOAD_TO = "default"

    # fields
    name = models.CharField(max_length=255, unique=False)
    mine_type = models.CharField(max_length=255, unique=False)
    data = models.FileField(upload_to=UPLOAD_TO_HANDLER)
    kind = models.CharField(max_length=255, unique=False, null=False, default=UPLOAD_TO)

    # generic foreign key
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = generic.GenericForeignKey()

    # special methods
    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return unicode(self.name)

    # django special methods
    @models.permalink
    def get_absolute_url(self):
        return "asset:serve", (self.pk,), {}

    @models.permalink
    def get_delete_url(self):
        return "asset:delete", (self.pk,), {}

    # interface
    def save(self, *args, **kwargs):
        super(Asset, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Asset, self).delete(*args, **kwargs)

    @classmethod
    def get_upload_path(cls, *args, **kwargs):
        return self.UPLOAD_PATH


if __name__ == "__main__":
    pass
