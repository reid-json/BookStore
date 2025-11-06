import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=20, default="guest+ " + str(uuid.uuid4))
    email = models.CharField(max_length=25, unique=True, primary_key=True)
    password = models.CharField(max_length=25)

