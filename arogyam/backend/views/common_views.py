from django.shortcuts import render, redirect
from django.db.models import Sum
from arogyam.backend.models import Product, Orderitems
from django.contrib import messages
from ..models import Users, Doctor

def home(request):
    user_type = request.session.get('user_type')
    user_id = request.session.get('user_id')

    trending_products = (
        Product.objects
        .annotate(total_sold=Sum('orderitems'))
        .order_by('-total_sold')[:5]  # Top 5 trending
    )
    if user_type == 'customer':
        user = Users.objects.get(userid=user_id)
        return render(request, 'home.html', {'user': user, 'trending_products': trending_products})
    # elif user_type == 'doctor':
    #     return redirect('doctor_dashboard')
    # elif user_type == 'admin':
    #     return redirect('admin_dashboard')
    else:
        return render(request, 'home.html', {'trending_products': trending_products})  # Guest view


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if role == 'customer':
            try:
                user = Users.objects.get(email=email, password=password)
                request.session['user_id'] = user.userid
                request.session['user_name'] = user.name
                request.session['user_type'] = 'customer'
                return redirect('customer_dashboard')
            except Users.DoesNotExist:
                messages.error(request, 'Invalid customer credentials.')

        elif role == 'doctor':
            try:
                doctor = Doctor.objects.get(email=email, fee=password)
                request.session['user_id'] = doctor.doctorid
                request.session['user_name'] = doctor.name
                request.session['user_type'] = 'doctor'
                return redirect('doctor_dashboard')
            except Doctor.DoesNotExist:
                messages.error(request, 'Invalid doctor credentials.')

        elif role == 'admin':
            # Example hardcoded admin (customize for real use)
            if email == 'admin' and password == 'admin123':
                request.session['user_type'] = 'admin'
                request.session['user_name'] = 'Admin'
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'Invalid admin credentials.')

    return render(request, 'auth/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        emailid= request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if role == 'customer':
            if Users.objects.filter(email=emailid).exists():
                messages.error(request, 'User already exists.')
            else:
                Users.objects.create(
                    name=username,
                    password=password,
                    email=emailid,
                )
                messages.success(request, 'Customer registered successfully.')
                return redirect('login')

        elif role == 'doctor':
            if Doctor.objects.filter(email=emailid).exists():
                messages.error(request, 'Doctor already exists.')
            else:
                Doctor.objects.create(
                    name=username,
                    fee=password,
                    email=emailid,
                    rating=0.0,
                    specialization='General'
                )
                messages.success(request, 'Doctor registered successfully.')
                return redirect('login')

        elif role == 'admin':
            messages.error(request, 'Admin cannot be registered here.')

    return render(request, 'auth/register.html')



def index(request):
    return render(request, "apitest.html")