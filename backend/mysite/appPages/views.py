from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the Book API</h1><p>Explore our catalog at /api/books/</p>")
