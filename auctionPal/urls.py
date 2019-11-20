from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from artifacts.views import ArtifactListView, ArtifactDetailView, ArtifactFeaturedListView, ArtifactFeaturedDetailView

from accounts.views import login_page, register_page, guest_register_view
from .views import index
from carts.views import cart_home
from bids.views import bid_list, bid_new
from addresses.views import checkout_address

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'login/$', login_page, name='login'),
    url(r'register/guest/$', guest_register_view, name='guest_register'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    url(r'bids/new/(?P<pk>\d+)/$', bid_new, name='bid_new'),
    url(r'^checkout/address/create/$', checkout_address, name='checkout_address'),
    url(r'bids/$', bid_list, name='bids'),
    url(r'mycart/$', cart_home, name='cart'),
    url(r'cart/', include("carts.urls", namespace='cart')),
    url(r'register/$', register_page, name='register'),
    # ModelListView as a callable item
    url(r'artifacts/$', ArtifactListView.as_view(), name='artifacts'),
    url(r'featured/$', ArtifactFeaturedListView.as_view(), name='featured'),
    # Checking the artifact primary key
    url(r'artifacts/(?P<pk>\d+)/$', ArtifactDetailView.as_view(), name='details'),
    url(r'featured/(?P<pk>\d+)/$',
        ArtifactFeaturedDetailView.as_view()),
    url(r'search/', include("search.urls", namespace='search')),
    # Admin url
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
