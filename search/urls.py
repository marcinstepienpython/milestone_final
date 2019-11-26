from django.conf.urls import url
from .views import (
    SearchArtifactListView
)
# search result url
urlpatterns = [
    url(r'^$', SearchArtifactListView.as_view(), name='query')
]
