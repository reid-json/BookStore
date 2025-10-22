from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BooksModel
from .serializers import BooksModelSerializer

class BooksListView(APIView):
    def get(self, request):
        books = BooksModel.objects.all()
        serializer = BooksModelSerializer(books, many=True)
        return Response(serializer.data)
