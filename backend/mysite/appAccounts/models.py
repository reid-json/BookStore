from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

