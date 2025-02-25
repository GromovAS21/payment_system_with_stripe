from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from items.models import Item
from items.stripe_services import StripeServices


class StripeGetSessionIdAPIView(GenericAPIView):
    """Получение id сессии Stripe"""

    queryset = Item.objects.all()

    def get(self, request, pk):
        item = self.get_object()
        item_name = item.name
        item_price = item.price
        stripe_item = StripeServices(item_name, item_price)
        stripe_product_id = stripe_item.stripe_create_product()
        stripe_price_id = stripe_item.stripe_create_price(stripe_product_id)
        stripe_session_id = stripe_item.stripe_create_session(stripe_price_id)
        return Response({"session_id": stripe_session_id})


def success_pay(request):
    """
    Страница с успешной оплатой
    """

    return render(request, "orders/success_pay.html")
