from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=64)
    slug = serializers.SlugField(max_length=64)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    is_active = serializers.BooleanField(default=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
