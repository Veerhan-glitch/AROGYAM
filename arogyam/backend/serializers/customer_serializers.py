from rest_framework import serializers
from arogyam.backend.models import Feedback, Booksappointment, Labtests, Prescription, Orders, Orderitems, Payments, Reports, Supporttickets, Notifications

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
