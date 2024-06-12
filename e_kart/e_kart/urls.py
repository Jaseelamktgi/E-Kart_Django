from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from e_kart import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include ('products.urls')),
    path('customers/',include ('customers.urls')),
    path('orders/',include ('orders.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)