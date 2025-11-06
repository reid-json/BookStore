from django.db import models
import uuid

class CartItem(models.Model):
    cart_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey('appCart.CartModel', on_delete=models.CASCADE, related_name='items')
    isbn = models.ForeignKey('appBooks.BooksModel', on_delete=models.CASCADE, db_column='isbn')
    quantity = models.PositiveIntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.isbn} in Cart {self.cart.cart_id}"