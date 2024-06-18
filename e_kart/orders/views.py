from django.shortcuts import render, redirect
from . models import Order, OrderedItem, Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='account')
def show_cart(request):
    user = request.user
    print(user)
    customer = user.customer_profile
    order ,created = Order.objects.get_or_create(
        owner=customer, 
        order_status=Order.CART_STAGE
    )
    context = {
        'cart':order
    }
    return render(request, 'cart.html', context)

@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        print(request.POST)
        # identify current user
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        size = request.POST.get('size')
        product_id = request.POST.get('product_id')
        
        # Find or create an order in the cart stage for the current user
        order, created = Order.objects.get_or_create(
            owner=customer, 
            order_status=Order.CART_STAGE,
            # defaults={'delete_status': Order.LIVE}
        )
        
        # Fetch the product instance
        product = Product.objects.get(id=product_id)

        # Check if the item is already in the cart
        ordered_item, created = OrderedItem.objects.get_or_create(
            product=product,
            owner=order,
            size=size
        )
        # If the item doesn't exists, create it
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        # If the item exists, increment the quantity  
        else:
            ordered_item.quantity =  ordered_item.quantity+quantity
            ordered_item.save()

        

        return redirect('cart')
    return render(request, 'cart.html')

@login_required(login_url='account')
def remove_item_from_cart(request,pk):
    ordered_item = OrderedItem.objects.get(id = pk)
    if ordered_item :
        ordered_item.delete()
    return render(request, 'cart.html')

@login_required(login_url='account')
def checkout_cart(request):
    if request.POST:
        try:
            # identify current user
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))
            size = request.POST.get('size')

            # Find or create an order in the cart stage for the current user
            order = Order.objects.get(
                owner=customer, 
                order_status=Order.CART_STAGE,
            )
            # Update order status
            if order :
                order.order_status = Order.ORDER_CONFIRMED
                order.total_price = total
                order.save()
                status_message = 'Order Confirmed. Your item will be delivered within 2 days.'
                messages.success(request, status_message)
            else:
                status_message = 'Order Not Confirmed. Please try again.' 
                messages.error(request, status_message)

        except Exception as e:
            status_message = 'Something went wrong. Please try again.'
            messages.error(request, status_message)

    return redirect('cart')

@login_required(login_url='account')
def show_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders = Order.objects.filter(owner = customer).exclude(order_status = Order.CART_STAGE)
    context = {
        'orders':all_orders
    }
    print(context)
    return render(request, 'orders.html', context)