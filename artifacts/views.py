# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView

from .models import Artifact
# Create your views here.


class ArtifactListView(ListView):
    queryset = Artifact.objects.all()
    template_name = 'artifacts/list.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ArtifactListView, self).get_context_data(**kwargs)
    #     return context


def artifact_list_view(request):
    queryset = Artifact.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'artifact/artifact_list_view.html', context)
