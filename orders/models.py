from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from items.models import Item


class Discount(models.Model):
    """Модель для скидок"""

    name = models.CharField(max_length=100, verbose_name="Название скидки")
    percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Процент скидки",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
        ordering = ("-id",)


class Tax(models.Model):
    """Модель для налогов"""

    name = models.CharField(max_length=100, verbose_name="Название налога")
    percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Процент налога",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Налог"
        verbose_name_plural = "Налоги"
        ordering = ("-id",)


class Order(models.Model):
    """Модель для заказов"""

    items = models.ManyToManyField(Item, verbose_name="Предметы заказа")
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Сумма заказа", blank=True, null=True, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Скидка",
    )
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Налог")
    currency = models.CharField(max_length=3, verbose_name="Валюта", blank=True, null=True, editable=False)

    def __str__(self):
        return f"Заказ Nо {self.pk}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ("-id",)
