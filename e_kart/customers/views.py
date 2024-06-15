from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Customers
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def show_account(request):
    context = {}
    # ========== User Registration  =========== :
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
        # Get form data
            print(request.POST)
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            
        # Check if user already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
                return render(request, 'account.html')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken.")
                return render(request, 'account.html')
            
        # Create user account | one to one relationship
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

        # Create customer profile
            customer = Customers.objects.create(user=user, address=address, phone=phone)
            customer.save()
            messages.success(request, "Account created successfully.")

        except Exception as e:
            # Handle duplicate username or email error
            error_message = str(e)
            messages.error(request,error_message)
            return render(request, 'account.html')

    # ========== User Login =========== :  
    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'account.html')

    return render(request, 'account.html',context)

#========== User Logout =========== :
def user_logout(request):
    logout(request)
    return redirect('home')
