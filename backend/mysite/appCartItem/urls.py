from django.urls import path
from .views import AddToCartView, RemoveFromCartView, ViewCartItems

urlpatterns = [
    path('cart/add/', AddToCartView.as_view(), name='cart-add'),
    path('cart/remove/', RemoveFromCartView.as_view(), name='cart-remove'),
    path('cart/view/', ViewCartItems.as_view(), name='cart-view'),
]