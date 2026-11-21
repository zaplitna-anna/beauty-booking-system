from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from users.permissions import IsMaster


class ServicesStatusView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "message": "Модуль послуг працює."
        })


class ServiceListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
            {
                "message": "Каталог послуг ще не підключено до бази даних."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )


class ServiceCreateView(APIView):
    permission_classes = [IsMaster]

    def post(self, request):
        return Response(
            {
                "message": "Створення послуг буде реалізовано після підключення моделі Service."
            },
            status=status.HTTP_501_NOT_IMPLEMENTED
        )
