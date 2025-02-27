from django.contrib import admin

from orders.models import Discount, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка для модели Order"""

    list_display = ("id", "total_price", "created_at", "discount")
    search_fields = ("id",)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """Админка для модели Discount"""

    list_display = ("id", "name", "discount_percent")
    search_fields = ("name",)
    list_filter = ("discount_percent",)
