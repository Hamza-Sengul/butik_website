from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Banner, ContactInfo, Contract, About
from django.contrib.auth.decorators import login_required
import random

def index(request):
    products = list(Product.objects.all())
    random.shuffle(products)
    banners = Banner.objects.all()
    contact_info = get_contact_info()
    return render(request, 'index.html', {'products': products, 'banners': banners, 'contact_info': contact_info})

@login_required
def hesabim(request):
    contact_info = get_contact_info()
    return render(request, 'hesabim.html', {'contact_info': contact_info})


def category_detail(request, category_name):
    contact_info = get_contact_info()
    category = Category.objects.get(name=category_name)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products, 'contact_info': contact_info})

def get_contact_info():
    return ContactInfo.objects.first()


def sozlesme(request):
    contact_info = get_contact_info()
    contract = Contract.objects.first()
    return render(request, 'sozlesme.html', {'contact_info': contact_info, 'contract': contract,})

def about_view(request):
    contact_info = get_contact_info()
    about = About.objects.first()
    context = {
        'about': about,
        'contact_info': contact_info,
    }
    return render(request, 'hakkimizda.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})
