# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from artifacts.models import Artifact
from django.db import models
from django.utils import timezone

# review model
class Review(models.Model):
    user = models.ForeignKey(User)
    artifact = models.ForeignKey(Artifact)
    title = models.CharField(max_length=200)
    review = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title
