import os

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from items.stripe_services import StripeServices
from orders.models import Order


class StripeGetSessionOrderIdAPIView(GenericAPIView):
    """Получение id сессии Stripe для заявки"""

    queryset = Order.objects.all()

    def get(self, request, pk):
        order = self.get_object()
        order_number = order
        order_price = order.total_price
        order_discount = order.discount.discount_percent if order.discount else None
        stripe_item = StripeServices(order_number, order_price, order_discount)
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
