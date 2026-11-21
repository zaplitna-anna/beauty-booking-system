import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from users.models import User, ua_phone_validator

class Booking(models.Model):

    class Status(models.TextChoices):
        CONFIRMED = "CONFIRMED", "Підтверджено"
        CANCELLED = "CANCELLED", "Скасовано"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="client_bookings",
        limit_choices_to={"role": "CLIENT"},
        null=True,
        blank=True,
        verbose_name="Клієнт"
    )

    master = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="master_bookings",
        limit_choices_to={"role": "MASTER"},
        verbose_name="Майстер"
    )

    service = models.ForeignKey(
        "services.Service",
        on_delete=models.PROTECT,
        related_name="bookings",
        verbose_name="Послуга"
    )

    date = models.DateField(
        "Дата відвідування"
    )

    start_time = models.TimeField(
        "Час початку"
    )

    end_time = models.TimeField(
        "Час завершення"
    )

    status = models.CharField(
        "Статус бронювання",
        max_length=10,
        choices=Status.choices,
        default=Status.CONFIRMED
    )

    customer_name = models.CharField(
        "Ім'я клієнта без облікового запису",
        max_length=150,
        blank=True
    )

    customer_phone = models.CharField(
        "Телефон клієнта без облікового запису",
        max_length=13,
        blank=True,
        validators=[ua_phone_validator]
    )

    def clean(self):
        super().clean()

        errors = {}

        if self.client_id:
            if self.client.role != User.Role.CLIENT:
                errors["client"] = (
                    "Обраний користувач не є клієнтом."
                )

        if self.master_id:
            if self.master.role != User.Role.MASTER:
                errors["master"] = (
                    "Обраний користувач не є майстром."
                )

        if self.service_id and self.master_id:
            if self.service.master_id != self.master_id:
                errors["service"] = (
                    "Обрана послуга не належить цьому майстру."
                )

        if self.service_id and self._state.adding:
            if not self.service.is_active:
                errors["service"] = (
                    "Не можна забронювати неактивну послугу."
                )

        if self.start_time and self.end_time:
            if self.start_time >= self.end_time:
                errors["end_time"] = (
                    "Час завершення має бути пізніше "
                    "часу початку."
                )

        if not self.client_id:
            if not self.customer_name.strip():
                errors["customer_name"] = (
                    "Вкажіть ім'я клієнта."
                )

            if not self.customer_phone.strip():
                errors["customer_phone"] = (
                    "Вкажіть номер телефону клієнта."
                )

        if errors:
            raise ValidationError(errors)

    def cancel(self):
        self.status = self.Status.CANCELLED
        self.save(update_fields=["status"])

    def __str__(self):
        return (
            f"{self.date} {self.start_time} — "
            f"{self.service.name}"
        )

    class Meta:
        verbose_name = "Бронювання"
        verbose_name_plural = "Бронювання"
        ordering = ["date", "start_time"]

        indexes = [
            models.Index(
                fields=["master", "date", "start_time"],
                name="booking_master_date_idx"
            )
        ]