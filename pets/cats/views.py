from django.shortcuts import render
from rest_framework import generics
from .serializers import CostSerializer
from .models import Cat
# Create your views here.

class 