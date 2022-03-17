from rest_framework.viewsets import ModelViewSet

from coupon.models.coupon import Coupon
from coupon.serializers.coupon import CouponSerializer
from auth_and_permissions.permissions import IsAuthenticatedReadOnly


class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticatedReadOnly]
    lookup_field = 'slug'
