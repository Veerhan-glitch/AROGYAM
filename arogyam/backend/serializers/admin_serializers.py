from rest_framework import serializers
from arogyam.backend.models import Users, Product, Offers, Useroffers

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
