from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # 🔐 Require login
from .models import BooksModel

class BooksAPIView(APIView):

    def get(self, request):
        books = BooksModel.objects.all()
        data = []
        for book in books:
            data.append({
                'isbn': book.isbn,
                'title': book.title,
                'genre': book.genre,
                'stock': book.stock,
                'author': book.author,
                'price': str(book.price),
                'coverImage': request.build_absolute_uri(book.coverImage.url),
                'published_date': book.published_date.isoformat(),
            })
        return Response(data)

class TestView(View):
    def get(self, request):
        return JsonResponse({"message": "Hello from Django!"})