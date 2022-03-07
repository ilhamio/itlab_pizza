from rest_framework import routers

from assortment.views.category import CategoryViewSet
from assortment.views.product import ProductViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)
