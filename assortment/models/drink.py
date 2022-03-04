from django.db import models

from const import DRINK_IMAGEFIELD_PATH
from assortment.models.product_abstract import Product


class Drink(Product):
    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'

    is_alcohol = models.BooleanField(default=False)
    image = models.ImageField(upload_to=DRINK_IMAGEFIELD_PATH, verbose_name='image')
    volume = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='volume')
