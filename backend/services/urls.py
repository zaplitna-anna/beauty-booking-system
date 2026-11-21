from django.urls import path

from .views import (
    ServicesStatusView,
    ServiceListView,
    ServiceCreateView,
)

urlpatterns = [
    path("status/", ServicesStatusView.as_view(), name="services-status"),
    path("", ServiceListView.as_view(), name="services-list"),
    path("create/", ServiceCreateView.as_view(), name="services-create"),
]
