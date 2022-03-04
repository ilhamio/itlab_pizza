from rest_framework import serializers

from assortment.models.pizza import Pizza
from assortment.serializers.product import ProductSerializer


class PizzaSerializer(ProductSerializer):
    diameter = serializers.DecimalField(max_digits=5, decimal_places=2)

    def create(self, validated_data):
        return Pizza.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.price = validated_data.get("name", instance.price)
        instance.description = validated_data.get("description", instance.description)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.updated = validated_data.get("updated", instance.updated)
        instance.diameter = validated_data.get("diameter", instance.diameter)
        instance.save()
        return instance
