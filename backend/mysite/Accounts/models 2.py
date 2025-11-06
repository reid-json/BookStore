from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=100), models.UUIDField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
