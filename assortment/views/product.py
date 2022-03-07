from rest_framework.viewsets import ModelViewSet

from assortment.models.product import Product
from assortment.serializers.product import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'