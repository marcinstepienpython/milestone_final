# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-11-24 21:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artifacts', '0008_auto_20191118_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='seller',
        ),
        migrations.AddField(
            model_name='artifact',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
