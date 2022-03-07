from django.urls import path, include

from order.router import router


urlpatterns = [
    path('', include(router.urls))
]
