from rest_framework import serializers

from order.models.order_item import OrderItem


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
        read_only_fields = ['order']

    quantity = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', 0)
        instance.save()
        return instance


class OrderItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['quantity']
        read_only_fields = ['product', 'order']

    quantity = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', 0)
        instance.save()
        return instance
