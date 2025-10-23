from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BooksModel
from .serializers import BooksModelSerializer

class BooksListView(APIView):
    @staticmethod
    def get(request):
        books = BooksModel.objects.all()
        serializer = BooksModelSerializer(books, many=True)
        serialized_data = serializer.data

        for i, book in enumerate(books):
            if book.cover_image:

                image_path = book.cover_image.decode('utf-8') if isinstance(book.cover_image, bytes) else str(book.cover_image)
                image_url = request.build_absolute_uri(f'/media/{image_path}')
                serialized_data[i]['cover_image'] = image_url
            else:
                serialized_data[i]['cover_image'] = None

        return Response(serialized_data)