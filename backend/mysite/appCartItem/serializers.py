from rest_framework import serializers
from appBooks.models import BooksModel
from appCartItem.models import CartItem
from appBooks.serializers import BooksModelSerializer  # if you have one

class CartItemSerializer(serializers.ModelSerializer):
    isbn = BooksModelSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['cart_item_id', 'isbn', 'quantity', 'added_date']

class AddCartItemSerializer(serializers.Serializer):
    isbn = serializers.CharField(max_length=13)
    quantity = serializers.IntegerField(min_value=1)