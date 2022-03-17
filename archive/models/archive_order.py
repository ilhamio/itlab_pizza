from django.db import models


class ArchiveOrder(models.Model):
    """Модель для архивирования выполненных заказов. После выдачи заказа создается
    модель ArchiveOrder на основании Order, а заказ в свою очередь удаляется из списка"""

    name_in_queue = models.CharField(max_length=64, blank=True, verbose_name='name in queue')
    place = models.SmallIntegerField(blank=True, null=True, verbose_name='number of place')
    coupon = models.CharField(max_length=255, verbose_name='coupon')
    comment = models.TextField(blank=True, verbose_name='comment')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    cost = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='cost')
    json_of_items = models.JSONField(verbose_name='items')

    class Meta:
        verbose_name = 'Архивированный заказ'
        verbose_name_plural = 'Архивированные заказы'

    def __str__(self):
        return self.id
