# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render

from artifacts.models import Artifact


class SearchArtifactListView(ListView):
    template_name = 'artifacts/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            return Artifact.objects.filter(title__icontains=query)
        return Artifact.objects.features()
