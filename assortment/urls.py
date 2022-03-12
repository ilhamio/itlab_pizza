from django.urls import path, include

from assortment.router import router

urlpatterns = [
    path('', include(router.urls)),
]
