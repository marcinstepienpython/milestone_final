# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Artifact
from carts.models import Cart


class ArtifactFeaturedListView(ListView):
    template_name = 'artifacts/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Artifact.objects.all().featured()


class ArtifactFeaturedDetailView(DetailView):
    template_name = 'artifacts/featured-details.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Artifact.objects.all().featured()


class ArtifactListView(ListView):
    template_name = 'artifacts/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Artifact.objects.all()


class ArtifactDetailView(DetailView):
    # queryset = Artifact.objects.all()
    template_name = 'artifacts/details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArtifactDetailView, self).get_context_data(*args, **kwargs)
        request = self.request
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Artifact.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Artifact does not exist")
        return instance
