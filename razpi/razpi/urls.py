
from django.contrib import admin
from django.urls import path
from core.views import frontpage,home,shop,about
from product.views import product
from cart.views import add_to_cart
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('home/',home, name="home"),
    path('shop/',shop,name="shop"),
    path('about/',about,name="about"),
    path('shop/<slug:slug>/', product, name="product"),
    path('add_to_cart/<int:product_id>/',add_to_cart, name="add_to_cart"),
    path(
        "razpi_icon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("razpi_icon.ico")),
    ),
]
