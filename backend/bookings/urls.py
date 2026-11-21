from django.urls import path

from .views import (
    BookingStatusView,
    AvailableSlotsView,
    BookingCreateView,
    ClientBookingsView,
    BookingCancelView,
    MasterBookingsView,
    ManualBookingView,
)

urlpatterns = [
    path("status/", BookingStatusView.as_view(), name="bookings-status"),

    path("available-slots/", AvailableSlotsView.as_view(), name="available-slots"),

    path("create/", BookingCreateView.as_view(), name="booking-create"),

    path("my/", ClientBookingsView.as_view(), name="my-bookings"),

    path(
        "<uuid:booking_id>/cancel/",
        BookingCancelView.as_view(),
        name="booking-cancel"
    ),

    path("master/", MasterBookingsView.as_view(), name="master-bookings"),

    path("manual/", ManualBookingView.as_view(), name="manual-booking"),
]