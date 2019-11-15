# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from artifacts.models import Artifact
# Create your models here.

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    artifacts = models.ManyToManyField(Artifact, blank=True)
    total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)