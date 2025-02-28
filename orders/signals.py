from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

from orders.models import Order


@receiver(m2m_changed, sender=Order.items.through)
def calculate_order_total_price(sender, instance, action, **kwargs) -> None:
    """Пересчитываем сумму заказа при добавлении/изменении/удалении предметов"""
    if action in ("post_add", "post_clear", "post_remove"):
        instance.total_price = sum(item.price for item in instance.items.all())
        instance.save(update_fields=["total_price"])


@receiver(m2m_changed, sender=Order.items.through)
def validate_item_currency(sender, instance, action, **kwargs) -> None:
    """Проверяем, что все предметы в заказе имеют одинаковую валюту"""
    if action == "post_add":
        item_currency = set(item.currency for item in instance.items.all())
        if len(item_currency) > 1:
            raise ValidationError("Валюта у предметов в заказе должна быть одинаковая")

        if item_currency:
            instance.currency = item_currency.pop()
            instance.save(update_fields=["currency"])
