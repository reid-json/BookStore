from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from appOrders.models import OrdersModel
from AA_StrategyPattern_PaymentInfo.PaymentContext import get_payment_strategy

class ProcessPaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get('order')
        method = request.data.get('method')
        card = request.data.get('card')


        order_items = OrdersModel.objects.filter(order_id=order_id, user=request.user)
        if not order_items.exists():
            return Response({ "error": "Order not found" }, status=404)


        total = sum(item.isbn.price * item.quantity for item in order_items)
        total = round(total, 2)


        try:
            strategy = get_payment_strategy(method)
        except ValueError as e:
            return Response({ "error": str(e) }, status=400)


        try:
            strategy.process_payment(user=request.user, amount=total, card=card)
        except Exception as e:
            return Response({ "error": f"Payment failed: {str(e)}" }, status=402)


        payment = Payment.objects.create(
            order=order_items.first(),
            amount=total,
            method=method,
            status='completed'
        )


        order_items.update(finalized=True)

        serializer = PaymentSerializer(payment)
        return Response(serializer.data)