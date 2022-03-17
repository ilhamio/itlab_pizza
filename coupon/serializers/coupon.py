from rest_framework import serializers

from coupon.models.coupon import Coupon


class CouponSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Coupon"""
    class Meta:
        model = Coupon
        fields = '__all__'
