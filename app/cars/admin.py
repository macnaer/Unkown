from django.contrib import admin

from .models import CarsList


class CarListAdmin(admin.ModelAdmin):
    list_display = ("id", "vendor", "model", "engine",
                    "color", "price", "rating", "carmanager_id", "is_published")
    list_display_links = ("id", "vendor", "model")
    list_editable = ("is_published",)
    search_fields = ("vendor", "price", "engine", "model", "rating")
    list_per_page = 25
    list_filter = ("carmanager_id", "vendor")


admin.site.register(CarsList, CarListAdmin)
