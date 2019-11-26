# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from artifacts.models import Artifact

# tag model
class Tag(models.Model):
    title = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
    artifacts = models.ManyToManyField(Artifact, blank=True)

    def __str__(self):
        return self.title
