from django.contrib import admin

from orders.models import Discount, Order, Tax


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка для модели Order"""

    list_display = ("id", "total_price", "created_at", "discount", "tax")
    search_fields = ("id",)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """Админка для модели Discount"""

    list_display = ("id", "name", "percent")
    search_fields = ("name",)
    list_filter = ("percent",)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    """Админка для модели Tax"""

    list_display = ("id", "name", "percent")
    search_fields = ("name",)
    list_filter = ("percent",)
