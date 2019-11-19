# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from artifacts.models import Artifact


class Bid(models.Model):
    user = models.ForeignKey(User)
    artifact = models.ForeignKey(Artifact)
    offer = models.DecimalField(decimal_places=2, max_digits=20, default=20)
    

    def __str__(self):
        return str(self.artifact)
