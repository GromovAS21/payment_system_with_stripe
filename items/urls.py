from django.urls import path

from items.apps import ItemsConfig
from items.views import StripeGetSessionItemIdAPIView, index, success_pay


app_name = ItemsConfig.name

urlpatterns = [
    path("buy/<int:pk>/", StripeGetSessionItemIdAPIView.as_view(), name="get_stripe_session_id"),
    path("success_pay/", success_pay, name="success_pay"),
    path("item/<int:pk>/", index, name="index"),
]
