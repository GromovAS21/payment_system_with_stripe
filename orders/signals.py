from django.db.models import Prefetch
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from items.models import Item
from orders.models import Order


@receiver(m2m_changed, sender=Order.items.through)
def calculate_order_total_price(sender, instance, action, **kwargs) -> None:
    """Пересчитываем сумму заказа при добавлении/изменении/удалении предметов"""
    if action in ("post_add", "post_clear", "post_remove"):
        instance = Order.objects.prefetch_related(Prefetch("items", queryset=Item.objects.only("price"))).get(
            pk=instance.pk
        )
        instance.total_price = sum(item.price for item in instance.items.all())
        instance.save(update_fields=["total_price"])
