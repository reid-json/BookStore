from django.db import models


# Create your models here.
class AccountModel(models.Model):
    username = models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, auto_created=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)