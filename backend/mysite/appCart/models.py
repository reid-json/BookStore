from django.db import models
from appAccounts.models import UserModel
from appBooks.models import BooksModel


# Create your models here.
class CartModel(models.Model):
    username = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cart_username')
    email = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cart_email', default= "")
    isbn = models.ForeignKey(BooksModel, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'email', 'isbn'],
                                    name='unique_cart')
        ]