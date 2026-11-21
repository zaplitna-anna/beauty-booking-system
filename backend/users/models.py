import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from .managers import UserManager

ua_phone_validator = RegexValidator(
    regex=r"^\+380\d{9}$",
    message="Введіть номер телефону у форматі +380XXXXXXXXX."
)

class User(AbstractUser):

    class Role(models.TextChoices):
        CLIENT = "CLIENT", "Клієнт"
        MASTER = "MASTER", "Майстер"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    username = None

    name = models.CharField("Ім'я", max_length=150)

    last_name = models.CharField(
        "Прізвище",
        max_length=150
    )

    email = models.EmailField(
        "Електронна пошта",
        unique=True
    )

    phone = models.CharField(
        "Номер телефону",
        max_length=13,
        validators=[ua_phone_validator]
    )

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.CLIENT
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone"]

    objects = UserManager()

    def __str__(self):
        return self.email
