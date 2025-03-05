from django import forms
from django.db.models import QuerySet


def validate_items(items: QuerySet) -> str:
    """Проверяем, что в заказе предметы с одной валютой"""
    if items:
        # Получаем валюты из списка предметов
        items_currency = set(item.currency for item in list(items))
        if len(items_currency) > 1:
            raise forms.ValidationError("Все предметы должны быть одной валюты.")

        return items_currency.pop()
