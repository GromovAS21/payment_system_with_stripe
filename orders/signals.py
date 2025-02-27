from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from orders.models import Order


@receiver(m2m_changed, sender=Order.items.through)
def calculate_order_total_price(sender, instance, action, **kwargs):
    """Пересчитываем сумму заказа при добавлении/изменении/удалении предметов"""
    if action in ("post_add", "post_remove", "post_clear"):
        instance.total_price = sum(item.price for item in instance.items.all())
        instance.save()
