# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf import settings
from django.db import models, migrations


def create_users(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split("."))

    # ADMIN
    user_admin = User()
    user_admin.username = "admin"
    user_admin.email = "spike-dev@g-node.org"
    user_admin.first_name = "Admin"
    user_admin.last_name = "User"
    user_admin.password = u"bcrypt_sha256$$2a$12$Xulmifg73.7y8GlVQtWL0.CeD.56zj962BOO0zEMtx49u/F5vthH6"
    user_admin.is_active = True
    user_admin.is_superuser = True
    user_admin.is_staff = True
    user_admin.save()


def change_site_id_one(apps, schema_editor):
    Site = apps.get_model("sites", "site")
    sites = Site.objects.all()
    for site in sites:
        if site.id == 1:
            site_id_one = site
            break
    else:
        site_id_one = Site()
    site_id_one.name = "G-Node Spike"
    site_id_one.domain = "spike.g-node.org"
    site_id_one.save()


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0001_initial"),
        ("sites", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(change_site_id_one),
        migrations.RunPython(create_users),
    ]

