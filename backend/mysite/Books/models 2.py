<<<<<<<< HEAD:backend/mysite/Books/models.py
#imports the models function from django
from django.db import models

#creates a table named Books_Model with certain attributes (title, price, author, stock, published_date).
#python version of sql kinda.
class BooksModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.CharField(max_length=100)
    stock = models.IntegerField()
    published_date = models.DateField()
========
>>>>>>>> d5dc5d0 (nothing):backend/mysite/mysite/Books/Models/BooksModel.py
