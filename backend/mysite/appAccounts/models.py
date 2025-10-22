from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        USER = 'user'
        ADMIN = 'admin'

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)

    @property
    def is_admin(self) -> bool:
        return self.role == self.Role.ADMIN or self.is_staff