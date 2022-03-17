from django.db import models

from assortment.models.product import Product
from order.models.order import Order


class OrderItem(models.Model):
    """Модель части заказа"""
    order = models.ForeignKey(Order, related_name='items', verbose_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.id} {self.product.name} {str(self.quantity)}'

    def get_cost(self):
        return self.product.price * self.quantity
