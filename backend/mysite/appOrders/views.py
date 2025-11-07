from collections import defaultdict
from uuid import uuid4
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings
from appCart.models import CartModel
from appCartItem.models import CartItem
from appOrders.models import OrdersModel
from appOrders.serializers import OrdersModelSerializer
from AA_StatePattern_Orders.OrderContext import get_order_state


class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        cart = CartModel.objects.get(user=user)
        items = CartItem.objects.filter(cart=cart)

        if not items.exists():
            return Response({ "error": "Cart is empty" }, status=400)

        order_uuid = uuid4()
        state = get_order_state('pending')  # Initial state

        try:
            for item in items:
                state.create(
                    user=user,
                    order_id=order_uuid,
                    isbn=item.isbn,
                    quantity=item.quantity
                )
            items.delete()

            # ✅ Send confirmation email
            send_mail(
                subject='Order Confirmation',
                message=f'Thank you for your order #{order_uuid}. We’ll notify you when it ships.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False
            )

            return Response({ "order_id": str(order_uuid) })

        except Exception as e:
            return Response({ "error": f"Order creation failed: {str(e)}" }, status=500)


class ListOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        orders = OrdersModel.objects.filter(user=request.user, finalized=True).order_by('-order_date')

        grouped = defaultdict(list)
        for order in orders:
            serialized = OrdersModelSerializer(order).data
            grouped[str(order.order_id)].append(serialized)

        response = [
            { "order_id": oid, "items": items }
            for oid, items in grouped.items()
        ]

        return Response(response)

