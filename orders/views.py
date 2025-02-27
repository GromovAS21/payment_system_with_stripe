import os

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from orders.models import Order
from services.stripe_services import StripeServices


class StripeGetSessionOrderIdAPIView(GenericAPIView):
    """Получение id сессии Stripe для заявки"""

    queryset = Order.objects.all()

    def get(self, request, pk):
        order = self.get_object()
        order_data = {
            "name": order,
            "price": order.total_price,
            "discount": order.discount.percent if order.discount else None,
            "tax": order.tax.percent if order.tax else None,
            "currency": order.currency,
        }
        stripe_item = StripeServices(**order_data)
        stripe_price_id = stripe_item.stripe_create_price()
        stripe_session_id = stripe_item.stripe_create_session(stripe_price_id)
        return Response({"session_id": stripe_session_id})


def index_order(request, pk: int) -> HttpResponse:
    """
    Страница для оплаты заказа
    """
    order = Order.objects.get(pk=pk)
    context = {"order": order, "publishable_stripe_key": os.getenv("STRIPE_PUBLISHABLE_KEY")}
    return render(request, "orders/index_order.html", context)
