# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Artifact(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    min_price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    deadline = models.DateTimeField()
    seller = models.ForeignKey(User)
    sold = models.BooleanField(default=False)


class Bid(models.Model):
    auction = models.ForeignKey(Artifact)
    user = models.ForeignKey(User)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default=0.50)


class Comment(models.Model):
    auction = models.ForeignKey(Artifact)
    user = models.ForeignKey(User)
    comment = models.TextField()
