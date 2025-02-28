from django.db import models


class CurrencyChoice(models.TextChoices):
    """Выбор валюты при создании товара"""

    RUB = "RUB", "RUB"
    USD = "USD", "USD"
    EUR = "EUR", "EUR"
