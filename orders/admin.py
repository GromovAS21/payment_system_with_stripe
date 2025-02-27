from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка для модели Order"""

    list_display = ("id", "total_price", "created_at")
    search_fields = ("id",)
