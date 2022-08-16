from django.contrib.auth import views
from django.urls import path, include
from cart.views import cart, checkout
from cart.views import add_to_cart


urlpatterns = [
path('cart/',cart,name="cart"),
path('checkout/',checkout,name="checkout"),
path('add_to_cart/<int:product_id>/',add_to_cart, name="add_to_cart"),
]