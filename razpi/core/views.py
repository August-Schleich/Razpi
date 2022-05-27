from django.shortcuts import render
from product.models import Product
def frontpage(request):
    return render(request, 'core/base.html')


def home(request):
    products = Product.objects.all()[0:8]
    return render(request,"core/home.html", {"products": products})