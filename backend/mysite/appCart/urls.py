from django.urls import path
from .views import UserCartView

urlpatterns = [
    path('cart/', UserCartView.as_view(), name='user-cart'),
]