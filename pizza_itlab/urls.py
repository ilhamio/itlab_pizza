from django.contrib import admin
from django.urls import path, include
from .swagger import urlpatterns as documentation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/assortment/', include('assortment.urls')),
    path('api/v1/order/', include('order.urls')),
    path('api/v1/coupon/', include('coupon.urls')),
    path('api/v1/archive/', include('archive.urls')),
    path('', include('rest_framework.urls'))
]

urlpatterns += documentation