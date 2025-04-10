import json, datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum, F, Count
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from arogyam.backend.models import *
from .serializers import *

# Home: Render the apitest.html page.
def index(request):
    return render(request, "apitest.html")

# ---------- CUSTOMER VIEWS ----------

@csrf_exempt
def feedback_by_user(request):
    # Expects POST with {"userid": ...}
    if request.method == "POST":
        data = json.loads(request.body)
        fb = Feedback.objects.filter(userid_id=data.get("userid"))
        serializer = FeedbackSerializer(fb, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def feedback_by_order(request):
    # Expects POST with {"orderid": ...}
    if request.method == "POST":
        data = json.loads(request.body)
        fb = Feedback.objects.filter(orderid_id=data.get("orderid"))
        serializer = FeedbackSerializer(fb, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_orders(request):
    # Expects POST with {"userid": ...}
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        orders = Orders.objects.filter(userid_id=userid)
        response = []
        for order in orders:
            items = Orderitems.objects.filter(orderid=order.orderid)
            total = sum(i.productid.price * i.quantity for i in items)
            order_data = OrderSerializer(order).data
            order_data["total_cost"] = total
            response.append(order_data)
        return JsonResponse(response, safe=False)

@csrf_exempt
def user_appointments(request):
    # Expects POST with {"userid": ...}
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        apps = Booksappointment.objects.filter(userid_id=userid)
        serializer = AppointmentSerializer(apps, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def prescriptions(request):
    # Expects POST with {"userid": ...}
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        presc = Prescription.objects.filter(userid_id=userid)
        serializer = PrescriptionSerializer(presc, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def book_appointment(request):
    # Expects POST with {"userid": ..., "doctorid": ..., "date": "YYYY-MM-DD", "type": ...}
    if request.method == "POST":
        data = json.loads(request.body)
        Booksappointment.objects.create(
            userid_id=data["userid"],
            doctorid_id=data["doctorid"],
            date=parse_date(data["date"]),
            type=data.get("type", ""),
            status="Scheduled"
        )
        return JsonResponse({"message": "Appointment booked"})
    
@csrf_exempt
def user_payments(request):
    # Expects POST with {"userid": ...}
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        order_ids = Orders.objects.filter(userid_id=userid).values_list("orderid", flat=True)
        payments = Payments.objects.filter(orderid__in=order_ids)
        serializer = PaymentSerializer(payments, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def lab_tests(request):
    # Expects POST with {"name": "..."} to search lab tests by name (only those available)
    if request.method == "POST":
        name = json.loads(request.body).get("name", "")
        tests = Labtests.objects.filter(name__icontains=name, status="Available")
        serializer = LabTestSerializer(tests, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def test_reports(request):
    # Expects POST with {"testid": ...}
    if request.method == "POST":
        testid = json.loads(request.body).get("testid")
        reports = Reports.objects.filter(testid_id=testid)
        serializer = ReportSerializer(reports, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def support_ticket(request):
    # Expects POST with {"userid": ..., "issuetype": ..., "description": ...}
    if request.method == "POST":
        data = json.loads(request.body)
        Supporttickets.objects.create(
            userid_id=data["userid"],
            issuetype=data["issuetype"],
            status="Open",
            description=data["description"]
        )
        return JsonResponse({"message": "Support ticket submitted"})
    
@csrf_exempt
def user_support_tickets(request):
    # Expects POST with {"userid": ...}
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        tickets = Supporttickets.objects.filter(userid_id=userid)
        serializer = SupportTicketSerializer(tickets, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_notifications(request):
    # Expects POST with {"userid": ...}
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        notes = Notifications.objects.filter(userid_id=userid).order_by("-datetime")
        serializer = NotificationSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_offers(request):
    # Expects POST with {"userid": ...}
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        offers = Useroffers.objects.filter(userid_id=userid)
        serializer = UserOfferSerializer(offers, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def search_products(request):
    # Expects POST with {"query": "..."}
    if request.method == "POST":
        query = json.loads(request.body).get("query", "")
        products = Product.objects.filter(Q(name__icontains=query) | Q(brand__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def product_details(request):
    # Expects POST with {"productid": ...}
    if request.method == "POST":
        pid = json.loads(request.body).get("productid")
        try:
            product = Product.objects.get(productid=pid)
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data, safe=False)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)

# ---------- DOCTOR VIEWS ----------

@csrf_exempt
def doctor_schedule(request):
    # Expects POST with {"doctorid": ..., "mode": "all"/"upcoming"/"completed"}
    if request.method == "POST":
        data = json.loads(request.body)
        doctorid = data.get("doctorid")
        mode = data.get("mode", "all")
        qs = Booksappointment.objects.filter(doctorid_id=doctorid)
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
        # create feedback (validation in model ensures order belongs to user)
        Feedback.objects.create(
            userid_id=data["userid"],
            orderid_id=data["orderid"],
            description=data["description"],
            rating=data["rating"]
        )
        return JsonResponse({"message": "Feedback submitted"})
    
@csrf_exempt
def health_records(request):
    # Expects POST with {"userid": ...} (patient id)
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        records = Healthrecords.objects.filter(userid_id=userid)
        serializer = HealthRecordSerializer(records, many=True)
        return JsonResponse(serializer.data, safe=False)

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
    # GET request returns all doctors
    docs = Doctor.objects.all()
    serializer = DoctorSerializer(docs, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def filter_doctors_by_specialization(request):
    # Expects POST with {"specialization": ...}
    if request.method == "POST":
        specialization = json.loads(request.body).get("specialization")
        docs = Doctor.objects.filter(specialization=specialization)
        serializer = DoctorSerializer(docs, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def sort_doctors_by_rating(request):
    # GET returns doctors sorted by rating descending
    docs = Doctor.objects.all().order_by("-rating")
    serializer = DoctorSerializer(docs, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def sort_doctors_by_fee(request):
    # GET returns doctors sorted by fee ascending
    docs = Doctor.objects.all().order_by("fee")
    serializer = DoctorSerializer(docs, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def get_specialization_values(request):
    # GET distinct specializations
    specs = Doctor.objects.values_list("specialization", flat=True).distinct()
    return JsonResponse(list(specs), safe=False)

# ---------- ADMIN VIEWS ----------

def all_users(request):
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def add_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = Users.objects.create(
            name=data["name"],
            email=data["email"],
            phonenumber=data["phonenumber"],
            password=data["password"],
            address=data.get("address", ""),
            age=data.get("age")
        )
        return JsonResponse({"message": "User created", "userid": user.userid})
    
@csrf_exempt
def delete_user(request, user_id):
    if request.method == "DELETE":
        try:
            user = Users.objects.get(userid=user_id)
            user.delete()
            return JsonResponse({"message": "User deleted"})
        except Users.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
    return JsonResponse({"error": "Invalid method"}, status=400)

@csrf_exempt
def add_product(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data["name"],
            brand=data["brand"],
            price=data["price"],
            composition=data["composition"],
            type=data["type"],
            prescriptionneeded=data["prescriptionneeded"]
        )
        return JsonResponse({"message": "Product added", "productid": product.productid})
    
@csrf_exempt
def update_product_price(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            product = Product.objects.get(productid=data["product_id"])
            product.price = data["new_price"]
            product.save()
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data, safe=False)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)
    
@csrf_exempt
def delete_product(request, product_id):
    if request.method == "DELETE":
        try:
            product = Product.objects.get(productid=product_id)
            product.delete()
            return JsonResponse({"message": "Product deleted"})
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)
    return JsonResponse({"error": "Invalid method"}, status=400)

def get_sales_by_month(request):
    sales = Orders.objects.values("date").annotate(
        revenue=Sum(F("orderitems__productid__price") * F("orderitems__quantity"))
    ).order_by("date")
    return JsonResponse(list(sales), safe=False)

def get_most_ordered_products(request):
    prod = Orderitems.objects.values("productid__name").annotate(
        times_ordered=Count("productid")
    ).order_by("-times_ordered")
    return JsonResponse(list(prod), safe=False)

@csrf_exempt
def add_lab_test(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lab_test = Labtests.objects.create(
            name=data["name"],
            price=data["price"],
            status=data["status"],
            testdetails=data["testdetails"]
        )
        serializer = LabTestSerializer(lab_test)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def link_report(request):
    if request.method == "POST":
        data = json.loads(request.body)
        report = Reports.objects.create(
            filepath=data["filepath"],
            testid_id=data["test_id"]
        )
        serializer = ReportSerializer(report)
        return JsonResponse(serializer.data, safe=False)
    
def all_offers(request):
    offers = Offers.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def send_notification(request):
    if request.method == "POST":
        data = json.loads(request.body)
        notif = Notifications.objects.create(
            userid_id=data["user_id"],
            message=data["message"],
            type=data["type"],
            datetime=datetime.datetime.now()
        )
        serializer = NotificationSerializer(notif)
        return JsonResponse(serializer.data, safe=False)

# Note: We remove an "assign offer" endpoint since offers are applied by the user at payment.
