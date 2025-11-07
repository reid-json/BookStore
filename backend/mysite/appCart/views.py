from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from appCart.models import CartModel
from .serializers import CartSerializer

class UserCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = CartModel.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)