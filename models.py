from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.contrib.auth.models import User
import uuid


class Food(models.Model):
    item = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name='post')
    descrption = models.CharField(max_length=300,default='',blank=True,null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='upload/images')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.item
