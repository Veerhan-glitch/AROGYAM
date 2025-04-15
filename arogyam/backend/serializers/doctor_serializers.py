from rest_framework import serializers
from arogyam.backend.models import Booksappointment, Doctor, Healthrecords

class BooksappointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booksappointment
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Healthrecords
        fields = '__all__'