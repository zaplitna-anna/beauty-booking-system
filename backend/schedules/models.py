
import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class WorkSchedule(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    master = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="work_schedules",
        limit_choices_to={"role": "MASTER"},
        verbose_name="Майстер"
    )

    date = models.DateField("Дата")

    is_day_off = models.BooleanField(
        "Вихідний день",
        default=False
    )

    def clean(self):
        super().clean()

        if self.master_id and self.master.role != "MASTER":
            raise ValidationError({
                "master": "Графік може належати лише майстру."
            })

    def __str__(self):
        return f"{self.date} — {self.master.name}"

    class Meta:
        verbose_name = "Робочий день"
        verbose_name_plural = "Робочі дні"
        ordering = ["date"]

        constraints = [
            models.UniqueConstraint(
                fields=["master", "date"],
                name="unique_master_schedule_date"
            )
        ]


class WorkInterval(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    schedule = models.ForeignKey(
        WorkSchedule,
        on_delete=models.CASCADE,
        related_name="intervals",
        verbose_name="Робочий день"
    )

    start_time = models.TimeField(
        "Початок роботи"
    )

    end_time = models.TimeField(
        "Завершення роботи"
    )

    def clean(self):
        super().clean()

        if (
            self.start_time is not None
            and self.end_time is not None
            and self.start_time >= self.end_time
        ):
            raise ValidationError({
                "end_time": (
                    "Час завершення має бути "
                    "пізніше часу початку."
                )
            })

        if self.schedule_id and self.schedule.is_day_off:
            raise ValidationError({
                "start_time": (
                    "Для вихідного дня не можна "
                    "вказувати робочі години."
                )
            })

    def __str__(self):
        return f"{self.start_time}–{self.end_time}"

    class Meta:
        verbose_name = "Робочий інтервал"
        verbose_name_plural = "Робочі інтервали"
        ordering = ["start_time"]
