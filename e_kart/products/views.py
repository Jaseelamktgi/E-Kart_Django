from django.shortcuts import render
from . models import Product

# Create your views here.
def home(request):
    return render (request, 'index.html')

def list_products(request):
    product_list = Product.objects.all()
    context = {'products':product_list}
    return render (request, 'products_list.html',context)

def product_details(request):
    return render (request, 'product_details.html')