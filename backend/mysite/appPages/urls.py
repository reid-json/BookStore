from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view),  # This handles the root of this app
]