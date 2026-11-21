import uuid
from decimal import Decimal

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

class Service(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    master = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="services",
        limit_choices_to={"role": "MASTER"},
        verbose_name="Майстер"
    )

    name = models.CharField(
        "Назва послуги",
        max_length=150
    )

    description = models.TextField(
        "Опис послуги"
    )

    price = models.DecimalField(
        "Вартість",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))]
    )

    duration_minutes = models.PositiveIntegerField(
        "Тривалість у хвилинах",
        validators=[MinValueValidator(1)]
    )

    is_active = models.BooleanField(
        "Активна",
        default=True
    )

    def clean(self):
        super().clean()

        if self.master_id and self.master.role != "MASTER":
            raise ValidationError({
                "master": "Послуга може належати лише майстру."
            })

    def deactivate(self):
        self.is_active = False
        self.save(update_fields=["is_active"])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"
        ordering = ["name"]