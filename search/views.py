from __future__ import unicode_literals
from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import render

from artifacts.models import Artifact


class SearchArtifactListView(ListView):
    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchArtifactListView,
                        self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            lookups = Q(title__icontains=query) | Q(
                description__icontains=query) | Q(year__icontains=query) | Q(origin__icontains=query)
            return Artifact.objects.filter(lookups).distinct()
        return Artifact.objects.features()
