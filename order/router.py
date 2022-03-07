from rest_framework import routers

from order.views.order import OrderViewSet

router = routers.DefaultRouter()
router.register(r'', OrderViewSet)
