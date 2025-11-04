#imports the models function from django


from django.db import models

#creates a table named Books_Model with certain attributes (title, price, author, stock, published_date).
#python version of sql kinda.
class BooksModel(models.Model):
    #ispn = models.UUIDField(max_length=13, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, auto_created=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.CharField(max_length=100)
    stock = models.IntegerField()
    published_date = models.DateField()
    cover_image = models.ImageField()