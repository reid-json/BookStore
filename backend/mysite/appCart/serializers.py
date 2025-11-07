from rest_framework import serializers
from appCart.models import CartModel
from appCartItem.models import CartItem
from appCartItem.serializers import CartItemSerializer

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = CartModel
        fields = ['cart_id', 'user', 'created_date', 'updated_date', 'items']
        read_only_fields = ['user']