from rest_framework.permissions import BasePermission

from .models import User


class IsClient(BasePermission):
    message = "Доступ дозволено лише клієнтам."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.CLIENT
        )


class IsMaster(BasePermission):
    message = "Доступ дозволено лише майстру."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.MASTER
        )
