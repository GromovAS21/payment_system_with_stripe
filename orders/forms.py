from django import forms

from orders.models import Order
from orders.validators import validate_items


class OrderForm(forms.ModelForm):
    """Форма для модели Order"""

    class Meta:
        model = Order
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        items = cleaned_data.get("items")
        currency = validate_items(items)
        self.instance.currency = currency
        return cleaned_data
