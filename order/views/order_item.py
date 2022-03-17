from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from auth_and_permissions.permissions import IsWaiter
from order.models.order_item import OrderItem
from order.serializers.order_item import OrderItemCreateSerializer, OrderItemUpdateSerializer
from order.views.utils import check_item


class OrderItemCreateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemCreateSerializer
    permission_classes = [IsWaiter]

    def create(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id', None)

        serializer = OrderItemCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.data['order_id'] = order_id

        order_item_instance = check_item(order_id, serializer.data['product'])
        if order_item_instance:
            serializer.update(order_item_instance, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        OrderItem.objects.create(product_id=serializer.data['product'], order_id=order_id,
                                 quantity=serializer.data['quantity'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = check_item(kwargs.get('order_id', None), kwargs.get('product', None))
        if instance:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'No such item'})


class OrderItemRetrieveUpdateViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemUpdateSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = check_item(kwargs.get('order_id', None), kwargs.get('product', None))
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({'error': 'No such item'})

    def update(self, request, *args, **kwargs):
        instance = check_item(kwargs.get('order_id', None), kwargs.get('product', None))
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
