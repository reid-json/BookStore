from django.db import models

class BooksModel(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    stock = models.IntegerField()
    author = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    coverImage = models.ImageField(upload_to='media/covers/')
    published_date = models.DateField()

    def __str__(self):
        return self.title
