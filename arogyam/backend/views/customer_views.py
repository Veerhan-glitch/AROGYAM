import json
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q, F, Max, DecimalField, OuterRef, Subquery, Count
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
from arogyam.backend.models import (
    Feedback, Booksappointment, Labtests, Prescription, Orders, 
    Orderitems, Payments, Reports, Supporttickets, Notifications, 
    Product, Useroffers, Doctor
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
def feedback_by_product(request):
    # Updated view: Instead of filtering by orderid, filter by productid.
    # This returns all feedback for a given product.
    if request.method == "POST":
        data = json.loads(request.body)
        fb = Feedback.objects.filter(productid_id=data.get("productid"))
        serializer = FeedbackSerializer(fb, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_orders(request):
    if request.method == "POST":
        userid = json.loads(request.body).get("userid")
        orders = Orders.objects.filter(userid_id=userid)
        response = []

        for order in orders:
            # Get items in the order
            items = Orderitems.objects.filter(orderid=order.orderid)
            item_list = []
            total = 0

            for item in items:
                product = item.productid
                subtotal = product.price * item.quantity
                total += subtotal
                item_list.append({
                    "product_id": product.productid,
                    "product_name": product.name,
                    "brand": product.brand,
                    "quantity": item.quantity,
                    "price_per_unit": float(product.price),
                    "subtotal": float(subtotal)
                })

            order_data = OrderSerializer(order).data
            order_data["total_cost"] = float(total)
            order_data["items"] = item_list
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

def highest_avg_rated_doctor_by_specialization(request):
    """
    Returns the doctor(s) with the highest average (here, current) rating in each specialization.
    
    This uses a subquery to compute the maximum rating for each specialization and then filters
    doctors to only those whose rating equals that maximum.
    """
    # Define a subquery that calculates the maximum rating for the specialization corresponding to the outer query.
    max_rating_subquery = Doctor.objects.filter(
        specialization=OuterRef('specialization')
    ).values('specialization').annotate(
        max_rating=Max('rating')
    ).values('max_rating')[:1]  # We only need one value

    # Annotate each doctor with the maximum rating for his/her specialization
    qs = Doctor.objects.annotate(
        highest_rating=Subquery(max_rating_subquery, output_field=DecimalField())
    ).filter(
        rating=F('highest_rating')
    )
    
    # Prepare the result: doctor ID, name as DoctorName, specialization, and avg_rating (same as rating here)
    result = list(qs.values(
        'doctorid',
        'specialization',
        doctorName=F('name'),
        avg_rating=F('rating')
    ))
    return JsonResponse(result, safe=False)

def doctors_with_total_visits(request):
    """
    Returns all doctors along with their total number of patient visits (appointments).
    """
    doctors = Doctor.objects.annotate(
        total_visits=Count('booksappointment', distinct=True)
    ).values(
        'doctorid',
        'specialization',
        'total_visits',
        doctorName=F('name')
    ).order_by('-total_visits')

    return JsonResponse(list(doctors), safe=False)

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

def customer_dashboard(request):
    return render(request, 'customer/customer_dashboard.html')

def order_history(request):
    orders = Orders.objects.filter(user=request.user).prefetch_related('orderitems')
    return render(request, 'customer/orders.html', {'orders': orders})