from django.conf.urls import url
from .views import (
    SearchArtifactListView
)

urlpatterns = [
    url(r'^$', SearchArtifactListView.as_view(), name='list')
]
