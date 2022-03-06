from django.db import models

from assortment.models.product_abstract import Product


class Coupon(Product):
    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    products = models.ManyToManyField(Product, related_name='coupons')

