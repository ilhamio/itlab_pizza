from django.db import models
from const import PIZZA_IMAGEFIELD_PATH
from assortment.models.product_abstract import Product


class Pizza(Product):
    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

    image = models.ImageField(upload_to=PIZZA_IMAGEFIELD_PATH, verbose_name='image')
    diameter = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='diameter')