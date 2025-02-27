from django.contrib import admin

from items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Админка для модели Item"""

    list_display = ("id", "name", "description", "price")
    search_fields = ("name",)
