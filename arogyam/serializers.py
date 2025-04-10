from rest_framework import serializers
from arogyam.backend.models import *

# Customer serializers
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctorid.name', read_only=True)
    class Meta:
        model = Booksappointment
        fields = '__all__'

class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labtests
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='productid.name', read_only=True)
    class Meta:
        model = Orderitems
        fields = ['orderitemid', 'orderid', 'productid', 'quantity', 'product_name']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'

class SupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supporttickets
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'

# Doctor serializer
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

# Admin serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['userid', 'name', 'age', 'email']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['productid']

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = '__all__'

class UserOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useroffers
        fields = '__all__'
