
from django.contrib import admin
from django.urls import path
from core.views import frontpage,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',frontpage,name="frontpage"),
    path('/home',home, name="home")
]
