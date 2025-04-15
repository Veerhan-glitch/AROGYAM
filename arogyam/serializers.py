from rest_framework import serializers
from .models import Booksappointment, Doctor, Users, Labtests

class BooksappointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booksappointment
        fields = ['appointmentid', 'userid', 'doctorid', 'date', 'type', 'status']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['doctorid', 'name', 'specialization', 'rating', 'fee']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['userid', 'name', 'email', 'phonenumber']

class LabtestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labtests
        fields = ['testid', 'name', 'price', 'status', 'testdetails']
