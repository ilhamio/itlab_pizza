from rest_framework.viewsets import ModelViewSet

from assortment.models.product import Product

from assortment.serializers.product import ProductSerializer
from auth_and_permissions.permissions import IsAuthenticatedReadOnly


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedReadOnly]
    lookup_field = 'slug'
