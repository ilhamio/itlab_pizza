from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from auth_and_permissions.permissions import IsAuthenticatedReadOnly, IsWaiter, IsCook, IsWaiterOrReadOnly
from coupon.models.coupon import Coupon
from archive.models.archive_order import ArchiveOrder
from order.models.order import Order
from order.serializers.order import OrderSerializer

from order.views.utils import check_order, change_status


class OrderViewSet(ModelViewSet):
    """ViewSet с CRUD операциями для модели Order"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsWaiterOrReadOnly]

    def list(self, request, *args, **kwargs):
        view = request.GET.get('view', '')
        if view == 'all':
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = self.filter_queryset(Order.objects.filter(is_registered=True))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance).data
        coupon = serializer['coupon']
        if coupon:
            serializer['coupon'] = Coupon.objects.get(code=coupon).__str__()
        serializer['cost'] = instance.get_total_cost()
        serializer['cost with coupon'] = instance.get_final_cost()
        return Response(serializer)


class OrderRegisterAPIView(views.APIView):
    """Регистрация заказа. Выполняется после добавления продуктов в заказ"""
    permission_classes = [IsWaiter]

    def get(self, request, *args, **kwargs):
        return change_status(2, **kwargs)


class OrderCompleteAPIView(views.APIView):
    """Завершение готовки заказа. Операция доступна только пользователям Cook"""
    permission_classes = [IsCook]

    def get(self, request, *args, **kwargs):
        return change_status(3, **kwargs)


class OrderFinishAPIView(views.APIView):
    """Выдача заказа клиенту. Операция доступна только Waiter.
    При выполнении удаляется модель Order и на ее основании делается ArchiveOrder"""
    permission_classes = [IsWaiter]

    def get(self, request, *args, **kwargs):
        instance = check_order(kwargs.get('order_id', None))
        if not instance:
            return Response({'error': 'No such order'})

        ArchiveOrder.objects.create(
            name_in_queue=instance.get_name_in_queue,
            place=instance.get_place,
            coupon=instance.get_coupon,
            comment=instance.get_comment,
            cost=instance.get_final_cost(),
            json_of_items=instance.get_items_dict()
        )
        Order.delete(instance)
        return Response({'success:' 'Заказ успешно архивирован'})
