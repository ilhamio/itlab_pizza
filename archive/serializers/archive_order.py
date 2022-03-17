from rest_framework import serializers

from archive.models.archive_order import ArchiveOrder


class ArchiveOrderSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели ArchiveOrder"""

    class Meta:
        model = ArchiveOrder
        fields = '__all__'
