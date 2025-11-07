from rest_framework import serializers
from appOrders.models import OrdersModel
from appBooks.serializers import BooksModelSerializer

class OrdersModelSerializer(serializers.ModelSerializer):
    isbn = BooksModelSerializer()

    class Meta:
        model = OrdersModel
        fields = ['order_id', 'isbn', 'quantity', 'order_date', 'status']