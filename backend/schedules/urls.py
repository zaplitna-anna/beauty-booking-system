
from django.urls import path

from .views import (
    ScheduleStatusView,
    MasterScheduleView,
    WorkingHoursView,
    DayOffView,
)


urlpatterns = [
    path("status/", ScheduleStatusView.as_view(), name="schedule-status"),

    path("", MasterScheduleView.as_view(), name="master-schedule"),

    path("working-hours/", WorkingHoursView.as_view(), name="working-hours"),

    path("days-off/", DayOffView.as_view(), name="days-off"),
]
