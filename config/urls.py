from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("items.urls", namespace="items")),
    path("", include("orders.urls", namespace="orders")),
]
