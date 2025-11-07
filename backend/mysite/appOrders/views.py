from collections import defaultdict
from uuid import uuid4
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from appCart.models import CartModel
from appCartItem.models import CartItem
from appOrders.models import OrdersModel
from appOrders.serializers import OrdersModelSerializer


class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        cart = CartModel.objects.get(user=user)
        items = CartItem.objects.filter(cart=cart)

        if not items.exists():
            return Response({ "error": "Cart is empty" }, status=400)

        order_uuid = uuid4()

        for item in items:
            OrdersModel.objects.create(
                order_id=order_uuid,
                user=user,
                isbn=item.isbn,
                quantity=item.quantity
            )

        items.delete()
        return Response({ "order_id": str(order_uuid) })

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

