from django.db import models

from assortment.models.category import Category


class Product(models.Model):
    """Product model for creating pizzas, drinks etc."""

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='category')
    name = models.CharField(max_length=64, verbose_name='name')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='slug')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    description = models.TextField(blank=True, verbose_name='description')
    is_active = models.BooleanField(default=True, verbose_name='is active')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated')
    size = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='size')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
