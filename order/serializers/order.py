from rest_framework import serializers

from coupon.models.coupon import Coupon
from order.models.order import Order


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True, read_only=True)
    final_price = serializers.DecimalField(max_digits=15, decimal_places=2, min_value=0.01, read_only=True)
    coupon = serializers.CharField()

    class Meta:
        model = Order
        read_only_fields = ['created', 'updated']
        fields = '__all__'

    def validate_place(self, value):
        if value:
            if value <= 0:
                return serializers.ValidationError("Not correct place value")
        return value

    def validate_coupon(self, value):
        if value:
            coupon = Coupon.objects.filter(code=value)
            if coupon:
                if coupon[0].is_valid():
                    return coupon[0]

        return serializers.ValidationError("Coupon is not valid!")
            