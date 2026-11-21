
from rest_framework import serializers

from .models import WorkSchedule, WorkInterval

class WorkIntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkInterval

        fields = [
            "id",
            "start_time",
            "end_time",
        ]

        read_only_fields = fields

class WorkScheduleSerializer(serializers.ModelSerializer):
    intervals = WorkIntervalSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = WorkSchedule

        fields = [
            "id",
            "master",
            "date",
            "is_day_off",
            "intervals",
        ]

        read_only_fields = fields