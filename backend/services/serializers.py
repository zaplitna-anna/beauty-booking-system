from rest_framework import serializers

from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service

        fields = [
            "id",
            "master",
            "name",
            "description",
            "price",
            "duration_minutes",
            "is_active",
        ]

        read_only_fields = ["id", "master"]