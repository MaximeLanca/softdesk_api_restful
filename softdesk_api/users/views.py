from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import generics
from users.models import CustomUser
from users.serializers import UserSerializer
from .serializers import RegisterSerializer

User = get_user_model()

class DataUserAPIView(APIView):
    def get (self, *args, **Kwargs):
        dataUser = CustomUser.objects.all()
        serializer = UserSerializer (dataUser, many=True)
        return Response (serializer.data)
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

