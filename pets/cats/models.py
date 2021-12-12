from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=64)
    about = models.TextField()
    age = models.FloatField()
    breed = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    owner = models.ForeignKey(get_user_model(),on_delete=CASCADE)

    def __str__(self) :
        return self.name