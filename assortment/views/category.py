from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from assortment.models.category import Category
from assortment.permissions import IsStaffOrReadOnly
from assortment.serializers.category import CategorySerializer
from assortment.serializers.product import ProductSerializer


class CategoryViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                      GenericViewSet):
    """Category ViewSet. CRUD operations with Category instances"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance).data
        product_serializer = ProductSerializer(instance.products.filter(is_active=True), many=True)
        serializer['product'] = product_serializer.data
        return Response(serializer)
