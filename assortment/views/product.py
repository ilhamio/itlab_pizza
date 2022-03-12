from rest_framework.viewsets import ModelViewSet

from assortment.models.product import Product
from assortment.permissions import IsStaffOrReadOnly
from assortment.serializers.product import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]
    lookup_field = 'slug'
