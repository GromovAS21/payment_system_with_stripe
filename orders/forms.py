from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        items = cleaned_data.get("items")
        items_currency = set(item.currency for item in list(items))
        if len(items_currency) > 1:
            raise forms.ValidationError("Все предметы должны быть в одной валюте.")
        self.instance.currency = items_currency.pop()

        return cleaned_data
