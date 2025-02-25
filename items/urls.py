from django.urls import path

from items.apps import ItemsConfig
from items.views import StripeGetSessionIdAPIView, success_pay


app_name = ItemsConfig.name

urlpatterns = [
    path("buy/<int:pk>/", StripeGetSessionIdAPIView.as_view(), name="get_stripe_session_id"),
    path("success_pay/", success_pay, name="success_pay"),
]
