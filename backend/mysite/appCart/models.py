from django.db import models
from appAccounts.models import AccountModel
from appBooks.models import BooksModel


# Create your models here.
class CartModel(models.Model):
    username = models.ForeignKey(AccountModel, on_delete=models.CASCADE, primary_key=True)
    ispn = models.ForeignKey(BooksModel, on_delete=models.CASCADE)