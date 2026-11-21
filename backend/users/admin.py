from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "name",
        "last_name",
        "phone",
        "role",
        "is_active",
        "is_staff",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )

    search_fields = (
        "email",
        "name",
        "last_name",
        "phone",
    )

    ordering = ("email",)

    readonly_fields = (
        "last_login",
        "date_joined",
    )

    fieldsets = (
        (
            "Обліковий запис",
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Особисті дані",
            {
                "fields": (
                    "name",
                    "last_name",
                    "phone",
                    "role",
                )
            },
        ),
        (
            "Права доступу",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Важливі дати",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            "Створення користувача",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "last_name",
                    "phone",
                    "role",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
