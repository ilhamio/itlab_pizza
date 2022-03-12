from rest_framework import serializers

from assortment.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model"""

    class Meta:
        model = Product
        fields = '__all__'
        read_only = ['created', 'updated']

    def validate_size(self, value):
        """validating size value"""
        if value <= 0:
            raise serializers.ValidationError("Not correct size value")
        return value

    def validate_price(self, value):
        """validating price value"""
        if value <= 0:
            raise serializers.ValidationError("Not correct price value")
        return value
