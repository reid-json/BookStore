from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('appBooks.urls')),
    path('', include('appAccounts.urls')),
    path('api/cartitem/', include('appCartItem.urls')),
    path('api/cart/', include('appCart.urls')),
    path('api/order/', include('appOrders.urls')),
    path('api/payment/', include('appPayment.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)