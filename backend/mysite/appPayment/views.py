from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from appOrders.models import OrdersModel

class ProcessPaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get('order')
        method = request.data.get('method')
        card = request.data.get('card')

        order_items = OrdersModel.objects.filter(order_id=order_id, user=request.user)
        if not order_items.exists():
            return Response({ "error": "Order not found" }, status=404)


        if method == "credit_card" and card and card.endswith("0000"):
            return Response({ "error": "Payment failed" }, status=402)


        total = sum(item.isbn.price * item.quantity for item in order_items)
        total = round(total, 2)


        payment = Payment.objects.create(
            order=order_items.first(),
            amount=total,
            method=method,
            status='completed'
        )

        # Finalize order
        OrdersModel.objects.filter(order_id=order_id, user=request.user).update(finalized=True)

        serializer = PaymentSerializer(payment)
        return Response(serializer.data)