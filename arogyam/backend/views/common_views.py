from datetime import date
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Sum
from arogyam.backend.models import Product, Orderitems
from django.contrib import messages
from rest_framework import generics
from arogyam.backend.serializers import BooksappointmentSerializer
from ..models import Booksappointment, Users, Doctor

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
        return redirect('customer_dashboard')
    elif user_type == 'doctor':
        return redirect('doctor_dashboard')
    elif user_type == 'admin':
        return redirect('admin_dashboard')
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
                doctor = Doctor.objects.get(email=email, password=password)
                request.session['user_id'] = doctor.doctorid
                request.session['user_name'] = doctor.name
                request.session['doctor_rating'] = float(doctor.rating)
                request.session['doctor_specialization'] = doctor.specialization
                request.session['user_type'] = 'doctor'
                return redirect('doctor_dashboard')
            except Doctor.DoesNotExist:
                messages.error(request, 'Invalid doctor credentials.')

        elif role == 'admin':
            # Example hardcoded admin (customize for real use)
            if email == 'admin@arogyam.com' and password == 'admin':
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
                    password=password,
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


def get_appointments(request):
    doctor_id = request.GET.get('doctorid')
    current_date = date.today()

    if doctor_id:
        # Check for the type filter parameter.
        # If provided and not equal to "all", filter appointments by the specified type.
        type_filter = request.GET.get('type')
        if type_filter and type_filter.lower() != "all":
            appointments = Booksappointment.objects.filter(doctorid=doctor_id).filter(type=type_filter)

        # Filter for today's appointments
        if 'today' in request.GET:
            appointments = Booksappointment.objects.filter(doctorid=doctor_id).filter(date=current_date)

        # Filter for upcoming appointments
        elif 'upcoming' in request.GET:
            from_date = request.GET.get('fromDate')
            to_date = request.GET.get('toDate')
            appointments = Booksappointment.objects.filter(doctorid=doctor_id).filter(date__gt=current_date)  # Only future appointments

            # Apply date range if provided
            if from_date:
                appointments = Booksappointment.objects.filter(doctorid=doctor_id).filter(date__gte=from_date)
            if to_date:
                appointments = Booksappointment.objects.filter(doctorid=doctor_id).filter(date__lte=to_date)

        # Filter for past appointments
        elif 'past' in request.GET:
            from_date = request.GET.get('fromDate')
            to_date = request.GET.get('toDate')
            appointments = Booksappointment.objects.filter(doctorid=doctor_id).filter(date__lt=current_date)  # Only past appointments

            # Apply date range if provided
            if from_date:
                appointments = Booksappointment.objects.filter(doctorid=doctor_id).filter(date__gte=from_date)
            if to_date:
                appointments = Booksappointment.objects.filter(doctorid=doctor_id).filter(date__lte=to_date)

        # Convert the query result to a list of dictionaries for JSON response
        appointment_list = list(appointments.values(
            'appointmentid', 'userid', 'doctorid', 'date', 'type', 'status'
        ))


        return JsonResponse(appointment_list, safe=False)

    return JsonResponse({"error": "Doctor ID is required."}, status=400)

def doctor_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')  # Redirect to login if not logged in

    doctor_id = request.session['user_id']
    doctor_name = request.session['user_name']
    doctor_rating = request.session.get('doctor_rating')
    doctor_specialization = request.session.get('doctor_specialization')

    return render(request, 'doctor_dashboard.html', {
        'doctor_id': doctor_id,
        'doctor_name': doctor_name,
        'doctor_rating': doctor_rating,
        'doctor_specialization': doctor_specialization
    })

def customer_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')  # Redirect to login if not logged in

    user_id = request.session['user_id']
    user_name = request.session['user_name']

    return render(request, 'customer_dashboard.html', {
        'user_id': user_id,
        'user_name': user_name
    })

def admin_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')  # Redirect to login if not logged in

    user_id = request.session['user_id']
    user_name = request.session['user_name']

    return render(request, 'admin_dashboard.html', {
        'user_id': user_id,
        'user_name': user_name
    })


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['user_name']
        del request.session['user_type']
    return redirect('login')












