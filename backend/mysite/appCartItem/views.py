from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from appBooks.models import BooksModel
from appCart.models import CartModel
from appCartItem.models import CartItem
from .serializers import CartItemSerializer, AddCartItemSerializer

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddCartItemSerializer(data=request.data)
        if serializer.is_valid():
            isbn = serializer.validated_data['isbn']
            quantity = serializer.validated_data['quantity']
            user = request.user

            try:
                book = BooksModel.objects.get(isbn=isbn)
            except BooksModel.DoesNotExist:
                return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

            if book.stock < quantity:
                return Response({'error': 'Not enough stock available'}, status=status.HTTP_400_BAD_REQUEST)

            cart, _ = CartModel.objects.get_or_create(user=user)
            item, created = CartItem.objects.get_or_create(cart=cart, isbn=book)

            if created:
                item.quantity = quantity
            else:
                if book.stock < quantity + item.quantity:
                    return Response({'error': 'Not enough stock to increase quantity'}, status=status.HTTP_400_BAD_REQUEST)
                item.quantity += quantity

            item.save()
            book.stock -= quantity
            book.save()

            return Response({'message': 'Book added to cart'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        isbn = request.data.get('isbn')
        user = request.user

        try:
            cart = CartModel.objects.get(user=user)
            item = CartItem.objects.get(cart=cart, isbn__isbn=isbn)
            book = item.isbn

            book.stock += item.quantity
            book.save()

            item.delete()
            return Response({'message': 'Book removed from cart'}, status=status.HTTP_200_OK)

        except (CartModel.DoesNotExist, CartItem.DoesNotExist, BooksModel.DoesNotExist):
            return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)


class ViewCartItems(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            cart = CartModel.objects.get(user=request.user)
            items = CartItem.objects.filter(cart=cart)
            serializer = CartItemSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CartModel.DoesNotExist:
            return Response([], status=status.HTTP_200_OK)