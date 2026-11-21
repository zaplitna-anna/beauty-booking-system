
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from users.permissions import IsClient, IsMaster

class BookingStatusView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "message": "Модуль бронювань працює."
        })

class AvailableSlotsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
            {
                "message": "Пошук вільних часових проміжків ще не реалізовано."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )

class BookingCreateView(APIView):
    permission_classes = [IsClient]

    def post(self, request):
        return Response(
            {
                "message": "Створення бронювання ще не реалізовано."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )

class ClientBookingsView(APIView):
    permission_classes = [IsClient]

    def get(self, request):
        return Response(
            {
                "message": "Перегляд власних бронювань ще не реалізовано."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )

class BookingCancelView(APIView):
    permission_classes = [IsClient]

    def post(self, request, booking_id):
        return Response(
            {
                "message": "Скасування бронювання ще не реалізовано."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )

class MasterBookingsView(APIView):
    permission_classes = [IsMaster]

    def get(self, request):
        return Response(
            {
                "message": "Перегляд бронювань майстром ще не реалізовано."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )

class ManualBookingView(APIView):
    permission_classes = [IsMaster]

    def post(self, request):
        return Response(
            {
                "message": "Ручне створення бронювання ще не реалізовано."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )