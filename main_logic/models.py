from django.contrib.auth.models import User
from django.db import models

ORDER_STATUS = {1: 'Подготовка заказа', 2: 'Приготовление', 3: 'Заказ готов', 4: 'Заказ выдан', 5: 'Ошибка'}
RANG_DICT = {1: 'waiter', 2: 'cook'}
PIZZA_DIAM_CHOICE = [('SMALL', 20), ('MEDIUM', 30), ('BIG', 40)]
DRINKS_VOL_CHOICE = [('SMALL', 0.3), ('MEDIUM', 0.5), ('BIG', 0.7)]
IMAGEFIELD_PATH = 'products'


class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=64, verbose_name='name')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='slug')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    description = models.TextField(blank=True, verbose_name='description')
    image = models.ImageField(upload_to=IMAGEFIELD_PATH, verbose_name='image')
    is_active = models.BooleanField(default=True, verbose_name='is active')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated')

    def __str__(self):
        return self.name


class Pizza(Product):
    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

    diameter = models.SmallIntegerField(choices=PIZZA_DIAM_CHOICE, verbose_name='diameter')


class Drinks(Product):
    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'

    volume = models.SmallIntegerField(choices=PIZZA_DIAM_CHOICE, verbose_name='diameter')


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    pass
