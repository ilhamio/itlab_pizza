from django.db import models

STATUS_CHOICES = (
    (1, 'Заказ принят'),
    (2, 'Заказ готовится'),
    (3, 'Заказ готов'),
    (4, 'Заказ выдан'),
)


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    name_in_queue = models.CharField(max_length=64, verbose_name='name in queue')
    is_registered = models.BooleanField(default=True, verbose_name='is registered')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated')
    paid = models.BooleanField(default=False, verbose_name='paid')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, verbose_name='status')

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
