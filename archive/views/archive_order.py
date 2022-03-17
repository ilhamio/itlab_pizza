from rest_framework.viewsets import ReadOnlyModelViewSet

from archive.models.archive_order import ArchiveOrder
from archive.serializers.archive_order import ArchiveOrderSerializer
from auth_and_permissions.permissions import IsAuthenticatedReadOnly


class ArchiveOrderReadOnlyViewSet(ReadOnlyModelViewSet):
    """ViewSet для модели ArchiveOrder"""
    queryset = ArchiveOrder.objects.all()
    serializer_class = ArchiveOrderSerializer
    permission_classes = [IsAuthenticatedReadOnly]  # Обычные сотрудники имеют доступ только к просмотру
