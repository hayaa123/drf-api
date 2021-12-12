from rest_framework import serializers
from .models import Cat

class CostSerializer(serializers.ModelSerializer):
    class Meta:
        fields =  ['name','about','age','color','owner']
        model = Cat


