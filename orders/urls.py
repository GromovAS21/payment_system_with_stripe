from django.urls import path

from orders.apps import OrdersConfig
from orders.views import StripeGetSessionOrderIdAPIView, index_order


app_name = OrdersConfig.name

urlpatterns = [
    path("buy/order/<int:pk>/", StripeGetSessionOrderIdAPIView.as_view(), name="stripe_order_session_id"),
    path("order/<int:pk>/", index_order, name="index_order"),
]
