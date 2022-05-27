
from django.contrib import admin
from django.urls import path
from core.views import frontpage,home,shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('home/',home, name="home"),
    path('shop/',shop,name="shop")
]
