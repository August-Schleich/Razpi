from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth import views

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    
    return render(request,'cart/menu_cart.html')
    
def cart(request):
    return render(request,'cart/cart.html')

@login_required
def checkout(request):
    return render(request,'cart/checkout.html')

# def login_checkout(request):
#       form = views.LoginView(request.POST)
#       if form.is_valid():
#             user = form.save()
#             login(request, user)
            
#             return redirect('cart/checkout')
#       return render (request, 'cart/login_checkout.html')