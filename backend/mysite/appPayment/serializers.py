from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'order', 'amount', 'method', 'status', 'timestamp']
        read_only_fields = ['payment_id', 'status', 'timestamp']