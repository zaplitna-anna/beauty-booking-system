from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[],
        error_messages={
            "required": "Вкажіть електронну пошту.",
            "blank": "Електронна пошта не може бути порожньою.",
            "invalid": "Введіть коректну електронну пошту.",
        }
    )

    password = serializers.CharField(
        write_only=True,
        error_messages={
            "required": "Вкажіть пароль.",
            "blank": "Пароль не може бути порожнім.",
        }
    )

    class Meta:
        model = User

        fields = [
            "id",
            "name",
            "last_name",
            "email",
            "phone",
            "password",
        ]

        read_only_fields = ["id"]

        extra_kwargs = {
            "name": {
                "error_messages": {
                    "required": "Вкажіть ім'я.",
                    "blank": "Ім'я не може бути порожнім.",
                }
            },
            "last_name": {
                "error_messages": {
                    "required": "Вкажіть прізвище.",
                    "blank": "Прізвище не може бути порожнім.",
                }
            },
            "phone": {
                "error_messages": {
                    "required": "Вкажіть номер телефону.",
                    "blank": "Номер телефону не може бути порожнім.",
                }
            },
        }

    def validate_email(self, value):
        email = value.strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                "Користувач із такою електронною поштою вже існує."
            )

        return email

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as error:
            raise serializers.ValidationError(error.messages)

        return value

    def create(self, validated_data):
        return User.objects.create_user(
            **validated_data,
            role=User.Role.CLIENT
        )

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        error_messages={
            "required": "Вкажіть електронну пошту.",
            "blank": "Вкажіть електронну пошту.",
            "invalid": "Введіть коректну електронну пошту.",
        }
    )

    password = serializers.CharField(
        write_only=True,
        error_messages={
            "required": "Вкажіть пароль.",
            "blank": "Вкажіть пароль.",
        }
    )

    def validate(self, attrs):
        email = attrs["email"].strip().lower()
        password = attrs["password"]

        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password
        )

        if user is None:
            raise serializers.ValidationError(
                "Неправильна електронна пошта або пароль."
            )

        attrs["user"] = user
        return attrs