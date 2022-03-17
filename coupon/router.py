from rest_framework import routers

from coupon.views.coupon import CouponViewSet

router = routers.DefaultRouter()
router.register(r'', CouponViewSet)
