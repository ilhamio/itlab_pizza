from rest_framework.viewsets import ModelViewSet

from order.models.order import Order
from order.serializers.order import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'slug'
