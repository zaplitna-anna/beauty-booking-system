from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from users.permissions import IsMaster


class ScheduleStatusView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "message": "Модуль управління розкладом працює."
        })


class MasterScheduleView(APIView):
    permission_classes = [IsMaster]

    def get(self, request):
        return Response(
            {
                "message": "Перегляд робочого графіка ще не реалізовано."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )


class WorkingHoursView(APIView):
    permission_classes = [IsMaster]

    def post(self, request):
        return Response(
            {
                "message": "Налаштування робочих годин буде реалізовано після підключення бази даних."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )


class DayOffView(APIView):
    permission_classes = [IsMaster]

    def post(self, request):
        return Response(
            {
                "message": "Налаштування вихідних днів буде реалізовано після підключення бази даних."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )
