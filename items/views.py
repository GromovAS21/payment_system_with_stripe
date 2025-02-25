import os

from django.http import HttpResponse
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
        stripe_price_id = stripe_item.stripe_create_price()
        stripe_session_id = stripe_item.stripe_create_session(stripe_price_id)
        return Response({"session_id": stripe_session_id})


def success_pay(request) -> HttpResponse:
    """
    Страница с успешной оплатой
    """

    return render(request, "items/success_pay.html")


def index(request, pk: int) -> HttpResponse:
    """
    Страница для оплаты
    """
    item = Item.objects.get(pk=pk)
    context = {"item": item, "publishable_stripe_key": os.getenv("STRIPE_PUBLISHABLE_KEY")}
    return render(request, "items/index.html", context)
