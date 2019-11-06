# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import random
import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 39999)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "artifacts/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ArtifactManager(models.Manager):

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class Artifact(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    min_price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    deadline = models.DateTimeField()
    seller = models.ForeignKey(User)
    sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    objects = ArtifactManager()

    def __str__(self):
        return self.title


class Bid(models.Model):
    auction = models.ForeignKey(Artifact)
    user = models.ForeignKey(User)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default=0.50)


class Comment(models.Model):
    auction = models.ForeignKey(Artifact)
    user = models.ForeignKey(User)
    comment = models.TextField()
