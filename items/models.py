from django.db import models

from items.choices import CurrencyChoice


class Item(models.Model):
    """Модель для предметов"""

    name = models.CharField(max_length=100, verbose_name="Название предмета")
    description = models.TextField(verbose_name="Описание предмета")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена предмета")
    currency = models.CharField(
        max_length=3, choices=CurrencyChoice.choices, default=CurrencyChoice.RUB, verbose_name="Валюта"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
        ordering = ("-id",)
