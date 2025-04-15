from rest_framework import serializers
from arogyam.backend.models import Booksappointment, Doctor

class BooksappointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booksappointment
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
