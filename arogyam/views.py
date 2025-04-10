from django.shortcuts import render
from django.http import JsonResponse
from .serializers import (
    FeedbackSerializer,
    AppointmentSerializer,
    LabTestSerializer,
    PrescriptionSerializer,
    OrderSerializer,
    DoctorSerializer,
)
from arogyam.backend.models import (
    Feedback,
    Booksappointment,
    Labtests,
    Prescription,
    Orders,
    Doctor,
)

def home(request):
    return render(request, 'apitest.html')

def get_feedback_by_order(request, order_id):
    feedback = Feedback.objects.filter(orderid_id=order_id)
    serializer = FeedbackSerializer(feedback, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_feedback_by_user(request, user_id):
    feedback = Feedback.objects.filter(userid_id=user_id)
    serializer = FeedbackSerializer(feedback, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_appointments(request, user_id):
    appointments = Booksappointment.objects.filter(userid_id=user_id)
    serializer = AppointmentSerializer(appointments, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_labtests(request, testid):
    # Now filter lab tests by testid only (instead of returning all).
    labtests = Labtests.objects.filter(testid=testid)
    serializer = LabTestSerializer(labtests, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_prescriptions(request, user_id):
    prescriptions = Prescription.objects.filter(userid_id=user_id)
    serializer = PrescriptionSerializer(prescriptions, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_orders_with_items(request, user_id):
    orders = Orders.objects.filter(userid_id=user_id)
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_all_doctors(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_doctors_by_specialization(request, specialization):
    doctors = Doctor.objects.filter(specialization__iexact=specialization)
    serializer = DoctorSerializer(doctors, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_doctors_sorted_by_rating(request):
    doctors = Doctor.objects.all().order_by('-rating')
    serializer = DoctorSerializer(doctors, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_doctors_sorted_by_fee(request):
    doctors = Doctor.objects.all().order_by('fee')
    serializer = DoctorSerializer(doctors, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_specializations(request):
    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    return JsonResponse(list(specializations), safe=False)

def get_appointments_by_doctor(request, doctor_id):
    """Return all appointments (Booksappointment) for a given doctor."""
    appointments = Booksappointment.objects.filter(doctorid_id=doctor_id)
    serializer = AppointmentSerializer(appointments, many=True)
    return JsonResponse(serializer.data, safe=False)
