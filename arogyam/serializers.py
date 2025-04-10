from rest_framework import serializers
from arogyam.backend.models import (
    Feedback,
    Booksappointment,
    Labtests,
    Prescription,
    Doctor,
    Orders,
    Orderitems,
    Product
)

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
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

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='productid.name', read_only=True)
    class Meta:
        model = Orderitems
        fields = ['product_name', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(source='orderitems_set', many=True, read_only=True)
    class Meta:
        model = Orders
        fields = ['orderid', 'date', 'status', 'trackinginfo', 'deliveryoption', 'order_items']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
