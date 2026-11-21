from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "start_time",
        "end_time",
        "client_name",
        "master",
        "service",
        "status",
    )

    list_filter = (
        "status",
        "date",
        "master",
        "service",
    )

    search_fields = (
        "client__email",
        "client__name",
        "customer_name",
        "customer_phone",
    )

    ordering = ("date", "start_time")

    readonly_fields = (
        "id",
        "client",
        "master",
        "service",
        "date",
        "start_time",
        "end_time",
        "status",
        "customer_name",
        "customer_phone",
    )

    def client_name(self, obj):
        if obj.client:
            return (
                f"{obj.client.name} "
                f"{obj.client.last_name}"
            )

        return obj.customer_name

    client_name.short_description = "Клієнт"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
