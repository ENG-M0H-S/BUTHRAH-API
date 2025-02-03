from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
        ('user', 'User'),
    )
    phone_number = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class PlantCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return self.name

class Plant(models.Model):
    category = models.ForeignKey(PlantCategory, on_delete=models.CASCADE, related_name='plants')
    name = models.CharField(max_length=100)
    information = models.TextField()
    image = models.ImageField(upload_to='plants/', null=True, blank=True)

    def __str__(self):
        return self.name
