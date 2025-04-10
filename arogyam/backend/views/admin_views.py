import json
from django.http import JsonResponse
from django.db.models import Sum, F, Count
from django.views.decorators.csrf import csrf_exempt
from arogyam.backend.models import (
    Users, Product, Orders, Orderitems, Labtests, Reports, Offers, 
    Notifications, Healthrecords
)
from arogyam.backend.serializers  import ProductSerializer, UserSerializer, OfferSerializer, UserSerializer

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
        from .serializers import LabTestSerializer
        serializer = LabTestSerializer(lab_test)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"error": "Invalid method"}, status=400)

@csrf_exempt
def link_report(request):
    if request.method == "POST":
        data = json.loads(request.body)
        from .serializers import ReportSerializer
        report = Reports.objects.create(
            filepath=data["filepath"],
            testid_id=data["test_id"]
        )
        serializer = ReportSerializer(report)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"error": "Invalid method"}, status=400)

def all_offers(request):
    from .serializers import OfferSerializer
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
