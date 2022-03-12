from django.db import models


class Category(models.Model):
    """Category model"""

    name = models.CharField(max_length=64, verbose_name='name')
    slug = models.CharField(max_length=64, unique=True, verbose_name='slug')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
