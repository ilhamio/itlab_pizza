from rest_framework.response import Response

from const import STATUS_CHOICES
from order.models.order import Order
from order.models.order_item import OrderItem


def check_item(order_id, product):
    if type(product) == int:
        instance = OrderItem.objects.filter(order_id=order_id, product_id=product)
    else:
        instance = OrderItem.objects.filter(order_id=order_id, product__slug=product)
    if instance:
        return instance[0]
    return None


def check_order(order_id):
    instance = Order.objects.filter(pk=order_id)
    if instance:
        return instance[0]
    return None


def change_status(value, **kwargs):
    instance = check_order(kwargs.get('order_id', None))
    print(instance.get_status)
    if not instance:
        return Response({'error': 'No such order'})

    instance.register()
    return Response({'success': f'Статус заказа {instance.id} изменен на "{STATUS_CHOICES[value][1]}"'})

