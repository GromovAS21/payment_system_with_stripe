from django.db import models

from items.models import Item


class Order(models.Model):
    """Модель для заказов"""

    items = models.ManyToManyField(Item, blank=True, verbose_name="Предметы заказа")
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Сумма заказа", blank=True, null=True, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")

    def __str__(self):
        return f"Заказ Nо {self.pk}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ("-id",)
