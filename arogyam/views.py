from django.shortcuts import render
from rest_framework import generics
from arogyam.backend.models import *
from .serializers import *

def home(request):
    return render(request, 'index.html')
