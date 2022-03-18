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
                raise serializers.ValidationError("Not correct place value")
        return value

    def validate_coupon(self, value):
        print(value)
        if value:
            coupon = Coupon.objects.filter(code=value)
            print(coupon, coupon[0])
            if coupon:
                if coupon[0].is_valid():
                    return coupon[0]

        raise serializers.ValidationError("Coupon is not valid!")
            