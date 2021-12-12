from django.db import models
from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import CatSerializer
from .models import Cat
# Create your views here.

class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class Catdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer