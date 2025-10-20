from django.db import models
from mysite import Cart


#creates a table named Cart_Model with certain attributes (username, password, cart).
#python version of sql kinda.
class AccountsModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    #cart = models.ForeignKey(Cart, on_delete=models.CASCADE)