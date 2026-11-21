
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from .models import WorkSchedule, WorkInterval


class WorkIntervalFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        if any(self.errors):
            return

        intervals = []

        for form in self.forms:
            if not form.cleaned_data:
                continue

            if form.cleaned_data.get("DELETE"):
                continue

            start = form.cleaned_data.get("start_time")
            end = form.cleaned_data.get("end_time")

            if start is not None and end is not None:
                intervals.append((start, end, form))

        if self.instance.is_day_off:
            for start, end, form in intervals:
                form.add_error(
                    "start_time",
                    "Для вихідного дня видаліть цей інтервал."
                )
            return

        if not intervals:
            raise ValidationError(
                "Для робочого дня додайте хоча б один часовий інтервал."
            )

        intervals.sort(key=lambda item: item[0])

        for index in range(1, len(intervals)):
            previous_end = intervals[index - 1][1]
            current_start = intervals[index][0]

            if current_start < previous_end:
                intervals[index][2].add_error(
                    "start_time",
                    "Робочі інтервали не можуть перекриватися."
                )


class WorkIntervalInline(admin.TabularInline):
    model = WorkInterval
    formset = WorkIntervalFormSet
    extra = 1


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "master",
        "is_day_off"
    )

    list_filter = ("is_day_off", "date")
    inlines = [WorkIntervalInline]
