from django.db import models


# Create your models here.
class AccountModel(models.Model):
    username = models.CharField(max_length=100, default= "")
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default= "")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'email'],
                                    name='unique_username_email')
        ]