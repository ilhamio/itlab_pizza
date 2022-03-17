import datetime
from decimal import Decimal

from django.db import models

from const import STATUS_CHOICES
from coupon.models.coupon import Coupon


class Order(models.Model):
    """Модель заказа"""
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    name_in_queue = models.CharField(max_length=64, blank=True, verbose_name='name in queue')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1, verbose_name='status')
    place = models.SmallIntegerField(blank=True, null=True, verbose_name='number of place')
    coupon = models.ForeignKey(Coupon, blank=True, null=True, related_name='orders', on_delete=models.SET_NULL)
    comment = models.TextField(blank=True, verbose_name='comment')
    is_registered = models.BooleanField(default=False, verbose_name='is registered')
    paid = models.BooleanField(default=False, verbose_name='paid')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated')

    def get_items_dict(self):
        items = self.items.all()
        d = dict()
        for i in items:
            d[i.product.name] = i.quantity
        return d

    def __str__(self):
        return self.name_in_queue

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_final_cost(self):
        price = self.get_total_cost()
        if self.coupon:
            return price - ((self.coupon.discount / Decimal('100')) * price)
        return price

    def register(self):
        self.status = 2
        self.save()

    def complete(self):
        self.status = 3
        self.save()

    def finish(self):
        self.status = 4
        self.save()

    @property
    def get_name_in_queue(self) -> str:
        return self.name_in_queue

    @property
    def get_place(self) -> int:
        return self.place

    @property
    def get_coupon(self) -> str:
        return self.coupon.__str__()

    @property
    def get_comment(self) -> str:
        return self.comment

    @property
    def get_status(self) -> int:
        return self.status

    @property
    def get_created(self) -> datetime:
        return self.created

    @property
    def get_updated(self) -> datetime:
        return self.updated

    @property
    def get_is_registered(self) -> bool:
        return self.is_registered

    @property
    def is_paid(self) -> bool:
        return self.is_paid
