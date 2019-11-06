# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Artifact
# Create your views here.


class ArtifactListView(ListView):
    template_name = 'artifacts/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Artifact.objects.all()


class ArtifactDetailView(DetailView):
    # queryset = Artifact.objects.all()
    template_name = 'artifacts/details.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Artifact.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Artifact does not exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Artifact.objects.filter(pk=pk)


# development
    # def get_context_data(self, **kwargs):
    #     context = super(ArtifactListView, self).get_context_data(**kwargs)
    #     return context


# def artifact_list_view(request):
#     queryset = Artifact.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, 'artifact/artifact_list_view.html', context)
