# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import base.models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=255)),
                ('data_orig_name', models.CharField(max_length=255)),
                ('data', models.FileField(upload_to=base.models.UPLOAD_TO_HANDLER)),
                ('kind', models.CharField(default='default', max_length=255)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('affiliation', models.CharField(default='', max_length=255)),
                ('research_area', models.TextField(default='')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
