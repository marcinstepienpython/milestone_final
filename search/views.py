# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render

from artifacts.models import Artifact


class SearchArtifactListView(ListView):
    template_name = 'artifacts/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Artifact.objects.all()
