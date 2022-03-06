from rest_framework import routers

from assortment.views.drink import DrinkViewSet
from assortment.views.pizza import PizzaViewSet
from assortment.views.coupon import CouponViewSet

router = routers.DefaultRouter()
router.register(r'pizza', PizzaViewSet)
router.register(r'drink', DrinkViewSet)
router.register(r'coupon', CouponViewSet)