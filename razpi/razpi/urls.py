
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import about, news

from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage



urlpatterns = [
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
    path('news/', news,name="news"),
    path('about/',about,name="about"),
    path('order/', include('order.urls'), name="order.urls"),
    path(
        "razpi_icon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("razpi_icon.ico")),
    ),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
