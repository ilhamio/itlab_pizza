
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from coupon.models.coupon import Coupon
from coupon.serializers import CouponSerializer


class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

