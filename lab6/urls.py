
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('shop.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^search-new/', include('shop.urls')),
    url(r'^search-basic/', include('shop.urls')),
    url(r'^search-sale/', include('shop.urls')),
    url(r'^reg/', include('shop.urls')),
    url(r'^login/', include('shop.urls')),
    url(r'^logout/', include('shop.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
