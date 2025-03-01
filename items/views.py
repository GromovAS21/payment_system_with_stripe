import os

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from items.models import Item
from services.stripe_services import StripeServices


class StripeGetSessionItemIdAPIView(GenericAPIView):
    """Получение id сессии Stripe для предмета"""

    queryset = Item.objects.all()

    def get(self, request, pk):
        item = self.get_object()
        item_data = {
            "name": item.name,
            "price": item.price,
            "currency": item.currency,
        }
        stripe_item = StripeServices(**item_data)
        stripe_price_id = stripe_item.stripe_create_price()
        stripe_session_id = stripe_item.stripe_create_session(stripe_price_id)
        return Response({"session_id": stripe_session_id}, status=status.HTTP_200_OK)


def success_pay(request) -> HttpResponse:
    """
    Страница с успешной оплатой
    """
    return render(request, "items/success_pay.html")


def index_item(request, pk: int) -> HttpResponse:
    """
    Страница для оплаты предмета
    """
    item = Item.objects.get(pk=pk)
    context = {"item": item, "publishable_stripe_key": os.getenv("STRIPE_PUBLISHABLE_KEY")}
    return render(request, "items/index_item.html", context)
