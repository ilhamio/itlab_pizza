from rest_framework import serializers

from assortment.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model"""

    class Meta:
        model = Category
        fields = '__all__'
