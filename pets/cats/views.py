from django.db import models
from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import CatSerializer
from .models import Cat
from .permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_class =(IsAuthenticatedOrReadOnly,)

class Catdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_class =(IsAuthenticatedOrReadOnly,)
