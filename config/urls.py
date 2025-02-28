from django.contrib import admin
from django.urls import include, path


admin.site.site_header = 'Администрирование "Платежного сервиса"'
admin.site.site_title = "Платежный сервис"
admin.site.index_title = "Администрирование"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("items.urls", namespace="items")),
    path("", include("orders.urls", namespace="orders")),
]
