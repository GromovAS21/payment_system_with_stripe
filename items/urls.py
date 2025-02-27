from django.urls import path

from items.apps import ItemsConfig
from items.views import StripeGetSessionItemIdAPIView, index_item, success_pay


app_name = ItemsConfig.name

urlpatterns = [
    path("buy/item/<int:pk>/", StripeGetSessionItemIdAPIView.as_view(), name="stripe_item_session_id"),
    path("success_pay/", success_pay, name="success_pay"),
    path("item/<int:pk>/", index_item, name="index_item"),
]
