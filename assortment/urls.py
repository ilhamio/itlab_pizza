from django.urls import path, include

from assortment.router import router

urlpatterns = [
    path('', include(router.urls)),  # Все CRUD операции для моделей assortment выполняются в роутере
]
