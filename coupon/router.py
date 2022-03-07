from rest_framework import routers

from coupon.views import CouponViewSet

router = routers.DefaultRouter()
router.register(r'', CouponViewSet)
