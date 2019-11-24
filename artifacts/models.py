# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db.models import Q
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
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename, ext=ext)
    return "artifacts/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ArtifactQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

    def sold(self):
        return self.filter(sold=False)

    def search(self, query):
        lookups = Q(title__icontains=query) | Q(
                description__icontains=query) | Q(year__icontains=query) | Q(origin__icontains=query) | Q(tag__title__icontains=query)
        
        return self.filter(lookups).distinct()

class ArtifactManager(models.Manager):
    # models manager
    def get_queryset(self):
        return ArtifactQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().sold()

    # featured artifacts (where featured==True)
    def features(self):
        return self.get_queryset().featured()
    # get artifact by id

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().all().search(query)


class Artifact(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    min_price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    deadline = models.DateTimeField()
    buyer = models.ForeignKey(User, null=True, blank=True)
    sold = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True)
    year = models.CharField(max_length=120, default='unknown')
    origin = models.CharField(max_length=120, default='unknown')
    featured = models.BooleanField(default=False)

    objects = ArtifactManager()
    
    def get_url(self):
        return '/artifacts/{pk}/'.format(pk=self.pk)


    def __str__(self):
        return self.title

    def set_status(self):
        self.sold = True
        self.save()
        return self.sold
    
    def set_buyer(self, user):
        self.buyer = user
        self.save()
        return self.buyer


# class Bid(models.Model):
#     auction = models.ForeignKey(Artifact)
#     user = models.ForeignKey(User)
#     amount = models.DecimalField(decimal_places=2, max_digits=20, default=0.50)

#     def __str__(self):
#         return self.amount


# class Comment(models.Model):
#     auction = models.ForeignKey(Artifact)
#     user = models.ForeignKey(User)
#     comment = models.TextField()

#     def __str__(self):
#         return self.comment
