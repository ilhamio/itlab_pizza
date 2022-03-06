from django.db import models

# Create your models here.
#
# class Coupon(models.Model):
#     pass
#
#
# class Order(models.Model):
#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
#
#     name_in_queue = models.CharField(max_length=64, verbose_name='name in queue')
#     date = models.DateTimeField(auto_now_add=True, verbose_name='date')
#     paid = models.BooleanField(default=True)
#
#     def __str__(self):
#         return 'Order {}'.format(self.id)
#
#     def get_total_cost(self):
#         return sum(item.get_cost() for item in self.items.all())
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', verbose_name='order')
#     product = models.ForeignKey(Product, related_name='order_items')
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return '{}'.format(self.id)
#
#     def get_cost(self):
#         return self.price * self.quantity