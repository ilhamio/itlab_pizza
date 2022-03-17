from django.urls import path

from archive.views.archive_order import ArchiveOrderReadOnlyViewSet

urlpatterns = [
    path('', ArchiveOrderReadOnlyViewSet.as_view({'get': 'list'})),  # Список архивированных заказов
    path('<int:order_id>/', ArchiveOrderReadOnlyViewSet.as_view({'get': 'retrieve'}))  # Только чтение записи по id
]
