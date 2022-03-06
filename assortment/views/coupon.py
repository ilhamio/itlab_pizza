from rest_framework.viewsets import ModelViewSet

from assortment.models.coupon import Coupon
from assortment.serializers.coupon import CouponSerializer


class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
