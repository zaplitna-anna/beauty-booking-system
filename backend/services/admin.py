
from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "master",
        "price",
        "duration_minutes",
        "is_active",
    )

    list_filter = (
        "is_active",
        "master",
    )

    search_fields = (
        "name",
        "description",
    )

    list_editable = ("is_active",)

    ordering = ("name",)
