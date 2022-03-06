from django.db import models
from assortment.models.product_abstract import Product


class Pizza(Product):
    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

    diameter = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='diameter')