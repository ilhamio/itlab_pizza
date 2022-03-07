from rest_framework.viewsets import ModelViewSet

from assortment.models.category import Category
from assortment.serializers.category import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

