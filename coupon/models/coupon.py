import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    """Модель купона для получения скидки на заказ"""
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return self.code

    @property
    def get_code(self) -> str:
        return self.code

    @property
    def get_valid_from(self) -> datetime.date:
        return self.valid_from

    @property
    def get_valid_to(self) -> datetime.date:
        return self.valid_to

    def set_active(self) -> None:
        if not self.is_valid():
            self.active = False

    def is_valid(self) -> bool:
        return bool(self.valid_from <= datetime.date.today() <= self.valid_to)
