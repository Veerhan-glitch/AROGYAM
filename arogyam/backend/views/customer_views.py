import json
from django.http import JsonResponse
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
from arogyam.backend.models import (
    Feedback, Booksappointment, Labtests, Prescription, Orders, 
    Orderitems, Payments, Reports, Supporttickets, Notifications, 
    Product, Useroffers
)
from arogyam.backend.serializers import (
    FeedbackSerializer, AppointmentSerializer, LabTestSerializer, 
    PrescriptionSerializer, OrderSerializer, OrderItemSerializer, 
    PaymentSerializer, ReportSerializer, SupportTicketSerializer, 
    NotificationSerializer, UserOfferSerializer, ProductSerializer
)

@csrf_exempt
def feedback_by_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        fb = Feedback.objects.filter(userid_id=data.get("userid"))
        serializer = FeedbackSerializer(fb, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def feedback_by_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        fb = Feedback.objects.filter(orderid_id=data.get("orderid"))
        serializer = FeedbackSerializer(fb, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_orders(request):
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
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        apps = Booksappointment.objects.filter(userid_id=userid)
        serializer = AppointmentSerializer(apps, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def prescriptions(request):
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        presc = Prescription.objects.filter(userid_id=userid)
        serializer = PrescriptionSerializer(presc, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def book_appointment(request):
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
    return JsonResponse({"error": "Invalid method"}, status=400)

@csrf_exempt
def user_payments(request):
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        order_ids = Orders.objects.filter(userid_id=userid).values_list("orderid", flat=True)
        payments = Payments.objects.filter(orderid__in=order_ids)
        serializer = PaymentSerializer(payments, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def lab_tests(request):
    if request.method == "POST":
        name = json.loads(request.body).get("name", "")
        tests = Labtests.objects.filter(name__icontains=name, status="Available")
        serializer = LabTestSerializer(tests, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def test_reports(request):
    if request.method == "POST":
        testid = json.loads(request.body).get("testid")
        reports = Reports.objects.filter(testid_id=testid)
        serializer = ReportSerializer(reports, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def support_ticket(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Supporttickets.objects.create(
            userid_id=data["userid"],
            issuetype=data["issuetype"],
            status="Open",
            description=data["description"]
        )
        return JsonResponse({"message": "Support ticket submitted"})
    return JsonResponse({"error": "Invalid method"}, status=400)

@csrf_exempt
def user_support_tickets(request):
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        tickets = Supporttickets.objects.filter(userid_id=userid)
        serializer = SupportTicketSerializer(tickets, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_notifications(request):
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        notes = Notifications.objects.filter(userid_id=userid).order_by("-datetime")
        serializer = NotificationSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_offers(request):
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        offers = Useroffers.objects.filter(userid_id=userid)
        serializer = UserOfferSerializer(offers, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def search_products(request):
    if request.method == "POST":
        query = json.loads(request.body).get("query", "")
        products = Product.objects.filter(Q(name__icontains=query) | Q(brand__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def product_details(request):
    if request.method == "POST":
        pid = json.loads(request.body).get("productid")
        try:
            product = Product.objects.get(productid=pid)
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data, safe=False)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)
