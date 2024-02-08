from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cagagory, Product  # Import the Product model

def home(request):
    return render(request, "shop/index.html")

def register(request):
    return render(request, "shop/register.html")

def collections(request):
    cagagory = Cagagory.objects.filter(status=0)
    return render(request, "shop/collections.html", {'cagagory': cagagory})

def collectionsview(request, name):
    if Cagagory.objects.filter(status=0).filter(name=name).exists():  # Check if the category exists
        products = Product.objects.filter(Cagagory__name=name)
        return render(request, "shop/collectionsview.html", {'products': products, 'category_name': name})
    else:
        messages.warning(request, "No Such Category Found")
        return redirect('collections')
