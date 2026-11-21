
from django.urls import path

from .views import (
    RegistrationView,
    LoginView,
    CurrentUserView,
    ClientAccessView,
    MasterAccessView,
    users_status,
)


urlpatterns = [
    path("status/", users_status, name="users-status"),

    path("register/", RegistrationView.as_view(), name="users-register"),

    path("login/", LoginView.as_view(), name="users-login"),

    path("me/", CurrentUserView.as_view(), name="users-me"),

    path("client-access/", ClientAccessView.as_view(), name="client-access"),

    path("master-access/", MasterAccessView.as_view(), name="master-access"),
]
