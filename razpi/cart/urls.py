from django.contrib.auth import views
from django.urls import path, include
from cart.views import cart, checkout
from cart.views import add_to_cart, hx_menu_cart, update_cart,hx_cart_total, success


urlpatterns = [
path('cart/',cart,name="cart"),
path('success/', success, name="success"),
path('checkout/',checkout,name="checkout"),
path('add_to_cart/<int:product_id>/',add_to_cart, name="add_to_cart"),
path('hx_menu_cart', hx_menu_cart, name="hx_menu_cart"),
path('hx_cart_total', hx_cart_total, name="hx_cart_total"),
path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),

]