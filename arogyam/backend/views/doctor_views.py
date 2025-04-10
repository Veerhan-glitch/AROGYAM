import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from arogyam.backend.models import Booksappointment, Feedback, Healthrecords, Doctor
from arogyam.backend.serializers import AppointmentSerializer, DoctorSerializer

@csrf_exempt
def doctor_schedule(request):
    # Expects POST with {"doctorid": ..., "mode": "all"/"upcoming"/"completed"}
    if request.method == "POST":
        data = json.loads(request.body)
        doctorid = data.get("doctorid")
        mode = data.get("mode", "all")
        qs = Booksappointment.objects.filter(doctorid_id=doctorid)
        today = Booksappointment.objects.filter().first().date  # fallback in case of error
        # Alternatively, import datetime and use datetime.date.today()
        import datetime
        today = datetime.date.today()
        if mode == "upcoming":
            qs = qs.filter(date__gte=today)
        elif mode == "completed":
            qs = qs.filter(status__iexact="Completed")
        serializer = AppointmentSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def doctor_feedback(request):
    # Expects POST with {"userid": ..., "orderid": ..., "description": ..., "rating": ...}
    if request.method == "POST":
        data = json.loads(request.body)
        Feedback.objects.create(
            userid_id=data["userid"],
            orderid_id=data["orderid"],
            description=data["description"],
            rating=data["rating"]
        )
        return JsonResponse({"message": "Feedback submitted"})

# @csrf_exempt
# def health_records(request):
#     # Expects POST with {"userid": ...}
#     if request.method == "POST":
#         userid = json.loads(request.body).get("userid")
#         records = Healthrecords.objects.filter(userid_id=userid)
#         serializer = HealthRecordSerializer(records, many=True)
#         return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def doctor_profile(request):
    # Expects POST with {"doctorid": ...}
    if request.method == "POST":
        docid = json.loads(request.body).get("doctorid")
        try:
            doc = Doctor.objects.get(doctorid=docid)
            serializer = DoctorSerializer(doc)
            return JsonResponse(serializer.data, safe=False)
        except Doctor.DoesNotExist:
            return JsonResponse({"error": "Doctor not found"}, status=404)

@csrf_exempt
def update_doctor_rating(request):
    # Expects POST with {"doctorid": ..., "new_rating": ...}
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            doc = Doctor.objects.get(doctorid=data["doctorid"])
            doc.rating = data["new_rating"]
            doc.save()
            serializer = DoctorSerializer(doc)
            return JsonResponse(serializer.data, safe=False)
        except Doctor.DoesNotExist:
            return JsonResponse({"error": "Doctor not found"}, status=404)

@csrf_exempt
def get_appointments_by_doctor(request):
    # Expects POST with {"doctorid": ...}
    if request.method == "POST":
        doctorid = json.loads(request.body).get("doctorid")
        qs = Booksappointment.objects.filter(doctorid_id=doctorid)
        serializer = AppointmentSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def all_doctors(request):
    docs = Doctor.objects.all()
    serializer = DoctorSerializer(docs, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def filter_doctors_by_specialization(request):
    # Expects POST with {"specialization": ...}
    if request.method == "POST":
        specialization = json.loads(request.body).get("specialization")
        docs = Doctor.objects.filter(specialization__iexact=specialization)
        serializer = DoctorSerializer(docs, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def sort_doctors_by_rating(request):
    # GET method, optionally accepts ?specialization=
    specialization = request.GET.get("specialization")
    qs = Doctor.objects.all()
    if specialization:
        qs = qs.filter(specialization__iexact=specialization)
    qs = qs.order_by("-rating")
    serializer = DoctorSerializer(qs, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def sort_doctors_by_fee(request):
    # GET method, optionally accepts ?specialization=
    specialization = request.GET.get("specialization")
    qs = Doctor.objects.all()
    if specialization:
        qs = qs.filter(specialization__iexact=specialization)
    qs = qs.order_by("fee")
    serializer = DoctorSerializer(qs, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def get_specialization_values(request):
    specs = Doctor.objects.values_list("specialization", flat=True).distinct()
    return JsonResponse(list(specs), safe=False)
