from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

def home(request):
    feautured_products = Product.objects.order_by('priority')[:4]  #displaying first priority 4 product
    latest_products = Product.objects.order_by('-id')[:4]  #displaying most visited 4 product in descending
    context = {
        'latest_products':latest_products,
        'feautured_products':feautured_products}
    # print(context)
    return render (request, 'index.html',context)

def list_products(request):
    product_list = Product.objects.order_by('priority')
    # pagination
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    product_paginator = Paginator(product_list, 4)     # Show 4 products per page
    product_list = product_paginator.get_page(page)
    context = {'products':product_list}
    return render (request, 'products_list.html',context)

def product_details(request,pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render (request, 'product_details.html',context)