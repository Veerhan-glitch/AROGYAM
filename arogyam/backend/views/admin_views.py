import json
from django.db.models import Max, Min, Sum, Avg, Subquery, OuterRef, DecimalField, F, Count, Q
from django.http import JsonResponse
from django.utils.timezone import now
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
from arogyam.backend.models import (
    Users, Product, Orders, Orderitems, Labtests, Reports, Offers, 
    Notifications, Healthrecords, Feedback, Payments, Doctor, Prescription, Booksappointment, Useroffers
)
from arogyam.backend.serializers  import ProductSerializer, UserSerializer, OfferSerializer, UserSerializer, LabTestSerializer, ReportSerializer, OfferSerializer

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
    return JsonResponse({"error": "Invalid method"}, status=400)

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

def get_most_ordered_products(request):
    prod = Orderitems.objects.values("productid__name").annotate(
        times_ordered=Count("productid")
    ).order_by("-times_ordered")[:10]
    return JsonResponse(list(prod), safe=False)

def users_with_orders_and_feedback(request):
    users = Users.objects.filter(
        userid__in=Orders.objects.values_list('userid', flat=True).distinct()
    ).filter(
        userid__in=Feedback.objects.values_list('userid', flat=True).distinct()
    ).values("userid", "name", "address", "age", "email", "phonenumber")
    return JsonResponse(list(users), safe=False)

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
    return JsonResponse({"error": "Invalid method"}, status=400)


def list_doctors_ratings(request):
    """
    Returns a list of doctors with their highest and lowest ratings.
    """
    # Group by DoctorID, Name, and Specialization then annotate with max and min ratings.
    doctors = Doctor.objects.values("doctorid", "name", "specialization").annotate(
        highest_rating=Max("rating"),
        lowest_rating=Min("rating")
    )
    return JsonResponse(list(doctors), safe=False)

def high_value_customers(request):
    # First, identify the OrderIDs where the total payment amount is greater than 500.
    order_ids = Payments.objects.values('orderid').annotate(
        total_amount=Sum('amount')
    ).filter(total_amount__gt=500).values_list('orderid', flat=True)

    # Now, get distinct UserIDs from Orders that have those OrderIDs.
    user_ids = Orders.objects.filter(orderid__in=order_ids).values_list('userid', flat=True).distinct()

    # Finally, fetch Users with these UserIDs and return their Name and Email.
    users = Users.objects.filter(userid__in=user_ids).values("name", "email")
    
    return JsonResponse(list(users), safe=False)
@csrf_exempt
def link_report(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = Users.objects.get(userid=data["userid"])
        report = Reports.objects.create(
            filepath="./report",
            testid_id=data["test_id"],
            userid=user,
        )
        serializer = ReportSerializer(report)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"error": "Invalid method"}, status=400)

def all_offers(request):
    offers = Offers.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def send_notification(request):
    if request.method == "POST":
        data = json.loads(request.body)
        import datetime
        notif = Notifications.objects.create(
            userid_id=data["user_id"],
            message=data["message"],
            type=data["type"],
            datetime=datetime.datetime.now()
        )
        from ..serializers import NotificationSerializer
        serializer = NotificationSerializer(notif)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"error": "Invalid method"}, status=400)

def top_revenue_products_for_prescription_users(request):
    """
    Returns the top 5 products that generated the most revenue from users who have prescriptions.
    Revenue = price * quantity (based on OrderItems)
    """
    # Step 1: Get User IDs who have prescriptions
    prescription_user_ids = Prescription.objects.values_list('userid', flat=True).distinct()

    # Step 2: Get Order IDs from those users
    order_ids = Orders.objects.filter(userid__in=prescription_user_ids).values_list('orderid', flat=True)

    # Step 3: Join OrderItems + Product, filter by those orders, and compute revenue
    product_revenue = Orderitems.objects.filter(orderid__in=order_ids).values(
        'productid', 'productid__name'
    ).annotate(
        total_revenue=Sum(F('productid__price') * F('quantity'))
    ).order_by('-total_revenue')[:5]

    # Step 4: Format response
    result = [
        {
            'productid': item['productid'],
            'name': item['productid__name'],
            'total_revenue': float(item['total_revenue'])
        }
        for item in product_revenue
    ]

    return JsonResponse(result, safe=False)


def recent_doctor_appointments_with_avg_fee(request):
    """
    For doctors with appointments in the last 360 days:
    - Show doctor ID, name, fee, appointment count
    - Include the average fee across all recent doctors
    """
    cutoff_date = now().date() - timedelta(days=360)

    recent_doctor_ids = Booksappointment.objects.filter(
        date__gte=cutoff_date
    ).values_list('doctorid', flat=True).distinct()

    avg_fee = Doctor.objects.filter(
        doctorid__in=recent_doctor_ids
    ).aggregate(avg_recent_fee=Avg('fee'))['avg_recent_fee'] or 0.0

    doctor_stats = Doctor.objects.filter(
        doctorid__in=recent_doctor_ids
    ).annotate(
        appointment_count=Count('booksappointment', filter=Q(booksappointment__date__gte=cutoff_date))
    ).values(
        'doctorid', 'name', 'fee', 'appointment_count'
    )

    for doc in doctor_stats:
        doc['avg_recent_doctor_fee'] = float(avg_fee)

    return JsonResponse(list(doctor_stats), safe=False)


def user_order_spending_with_offers(request):
    """
    Returns users who have used offers, along with total amount spent and order count.
    """
    offer_user_ids = Useroffers.objects.values_list('userid', flat=True).distinct()

    users = Users.objects.filter(userid__in=offer_user_ids).annotate(
        total_spent=Sum(
            F('orders__orderitems__quantity') * F('orders__orderitems__productid__price'),
            output_field=DecimalField()
        ),
        order_count=Count('orders__orderid', distinct=True)
    ).values(
        'userid',
        'name',
        'total_spent',
        'order_count'
    )

    for user in users:
        user['total_spent'] = float(user['total_spent'] or 0.0)

    return JsonResponse(list(users), safe=False)

def users_with_recent_activity(request):
    """
    Identify users who have either received notifications or placed orders
    within the last 12 months. Returns most recent activity date.
    """
    from_date = now() - timedelta(days=365)

    users = Users.objects.annotate(
        last_notif=Max(
            'notifications__datetime',
            filter=Q(notifications__datetime__gte=from_date)
        ),
        last_order=Max(
            'orders__date',
            filter=Q(orders__date__gte=from_date)
        )
    ).filter(
        Q(last_notif__isnull=False) | Q(last_order__isnull=False)
    ).values('userid', 'name', 'last_notif', 'last_order')

    result = []
    for user in users:
        last_notif = user['last_notif']
        last_order = user['last_order']
        last_active = max(filter(None, [last_notif, last_order]))  # ignore None values
        result.append({
            'userid': user['userid'],
            'name': user['name'],
            'last_active': last_active
        })

    result.sort(key=lambda x: x['last_active'], reverse=True)

    return JsonResponse(result, safe=False)

def users_who_ordered_prescription_products(request):
    """
    Returns users who have placed orders containing prescription-required products.
    """
    users = Users.objects.filter(
        orders__orderitems__productid__prescriptionneeded=True
    ).distinct().values('userid', 'name')

    return JsonResponse(list(users), safe=False)


def patient_medical_summary(request):
    """
    Returns a summary per user: doctor, appointment status, lab test info, and prescription ID.
    """
    data = []

    users = Users.objects.all().order_by('name')

    for user in users:
        appointments = Booksappointment.objects.filter(userid=user).select_related('doctorid')
        prescriptions = Prescription.objects.filter(userid=user)
        reports = Reports.objects.filter(testid__in=Labtests.objects.all())
        
        # We'll get only one row per user (latest info)
        for appt in appointments:
            data.append({
                "User ID": user.userid,
                "Patient Name": user.name,
                "Doctor": appt.doctorid.name if appt.doctorid else None,
                "Appt. Status": appt.status,
                "Lab Test": None,         # Updated below if found
                "Test Status": None,
                "Prescription ID": None   # Updated below if found
            })

        if not appointments:
            data.append({
                "User ID": user.userid,
                "Patient Name": user.name,
                "Doctor": None,
                "Appt. Status": None,
                "Lab Test": None,
                "Test Status": None,
                "Prescription ID": None
            })

        # Add Lab Test info (if any report is linked)
        labtests = Labtests.objects.filter(
            reports__in=Reports.objects.filter(testid__isnull=False)
        ).distinct()

        if labtests.exists():
            data[-1]["Lab Test"] = labtests.first().name
            data[-1]["Test Status"] = labtests.first().status

        if prescriptions.exists():
            data[-1]["Prescription ID"] = prescriptions.first().prescriptionid

    return JsonResponse(data, safe=False)


def user_order_history(request):
    """
    Returns full order history: user info, orders, products, quantity, payments.
    """
    order_items = Orderitems.objects.select_related(
        'orderid__userid',
        'productid',
        'orderid'
    ).order_by('-orderid__orderid')

    result = []
    for item in order_items:
        order = item.orderid
        user = order.userid
        product = item.productid

        # Get payment for this order
        payment = Payments.objects.filter(orderid=order).first()

        result.append({
            "User ID": user.userid,
            "Customer": user.name,
            "Order ID": order.orderid,
            "Order Status": order.status,
            "Product": product.name,
            "Qty": item.quantity,
            "Paid": float(payment.amount) if payment else None,
            "Payment Status": payment.status if payment else None
        })

    return JsonResponse(result, safe=False)