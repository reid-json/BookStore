from django.db import models
from appAccounts.models import AccountModel
from appBooks.models import BooksModel


# Create your models here.
class CartModel(models.Model):
    username = models.ForeignKey(AccountModel, on_delete=models.CASCADE, related_name='cart_username')
    email = models.ForeignKey(AccountModel, on_delete=models.CASCADE, related_name='cart_email')
    ispn = models.ForeignKey(BooksModel, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'email', 'ispn'],
                                    name='unique_cart')
        ]