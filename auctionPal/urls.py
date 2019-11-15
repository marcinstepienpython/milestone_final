from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

from artifacts.views import ArtifactListView, ArtifactDetailView, ArtifactFeaturedListView, ArtifactFeaturedDetailView

from .views import index, login_page, register_page
from carts.views import cart_home

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'login/$', login_page, name='login'),
     url(r'cart/$', cart_home, name='cart'),
    url(r'register/$', register_page, name='register'),
    # ModelListView as a callable item
    url(r'artifacts/$', ArtifactListView.as_view(), name='artifacts'),
    url(r'featured/$', ArtifactFeaturedListView.as_view(), name='featured'),
    # Checking the artifact primary key
    url(r'artifacts/(?P<pk>\d+)/$', ArtifactDetailView.as_view()),
    url(r'featured/(?P<pk>\d+)/$', ArtifactFeaturedDetailView.as_view()),
    url(r'search/', include("search.urls", namespace='search')),
    # Admin url
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
