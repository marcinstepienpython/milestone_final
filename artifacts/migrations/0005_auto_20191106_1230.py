# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-11-06 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0004_auto_20191106_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='artifact',
            name='origin',
            field=models.CharField(default='unknown', max_length=120),
        ),
        migrations.AddField(
            model_name='artifact',
            name='year',
            field=models.CharField(default='unknown', max_length=120),
        ),
    ]
