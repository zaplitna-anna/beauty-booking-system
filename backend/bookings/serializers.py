
from rest_framework import serializers

from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    status_label = serializers.CharField(
        source="get_status_display",
        read_only=True
    )

    class Meta:
        model = Booking

        fields = [
            "id",
            "client",
            "master",
            "service",
            "date",
            "start_time",
            "end_time",
            "status",
            "status_label",
            "customer_name",
            "customer_phone",
        ]

        read_only_fields = fields