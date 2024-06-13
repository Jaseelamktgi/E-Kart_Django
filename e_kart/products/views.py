from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

def home(request):
    return render (request, 'index.html')

def list_products(request):
    product_list = Product.objects.all()
    # Show 2 products per page
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    product_paginator = Paginator(product_list, 4) 
    product_list = product_paginator.get_page(page)
    context = {'products':product_list}
    return render (request, 'products_list.html',context)

def product_details(request):
    return render (request, 'product_details.html')