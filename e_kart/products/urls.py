from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('list_products', views.list_products, name= 'list_products'),
    path('product_details', views.product_details, name= 'product_details'),
]