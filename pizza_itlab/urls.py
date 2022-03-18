from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from .swagger import urlpatterns as documentation


def index(request):
    return HttpResponse(
        "Доброго времени суток! К сожалению, красивого фронта в проекте нет, но суть ведь не в этом, правда?")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/assortment/', include('assortment.urls')),
    path('api/v1/order/', include('order.urls')),
    path('api/v1/coupon/', include('coupon.urls')),
    path('api/v1/archive/', include('archive.urls')),
    path('accounts/', include('rest_framework.urls')),
    path('', index)
]

urlpatterns += documentation
