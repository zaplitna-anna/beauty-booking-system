from .permissions import IsClient, IsMaster
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import LoginSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def users_status(request):
    return Response({
        "message": "Модуль користувачів працює"
    })


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]
    

class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "Вхід виконано успішно.",
            "token": token.key,
            "role": user.role
        })

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "id": str(user.id),
            "name": user.name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role
        })
        

class ClientAccessView(APIView):
    permission_classes = [IsClient]

    def get(self, request):
        return Response({
            "message": "Вітаємо в кабінеті клієнта!",
            "name": request.user.name
        })


class MasterAccessView(APIView):
    permission_classes = [IsMaster]

    def get(self, request):
        return Response({
            "message": "Вітаємо в панелі майстра!",
            "name": request.user.name
        })

