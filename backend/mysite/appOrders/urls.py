from django.urls import path
from .views import PlaceOrderView, ListOrdersView

urlpatterns = [
    path('place/', PlaceOrderView.as_view(), name='place-order'),
    path('list/', ListOrdersView.as_view(), name='list-orders'),
]