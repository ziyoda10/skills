# from rest_framework import generics
# from .models import User
# from .serializers import RegisterSerializer, UserSerializer
# from rest_framework.permissions import IsAuthenticated


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer


# class ProfileView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny] # Hamma ro'yxatdan o'ta olishi uchun

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            return Response({"error": "Username va password yuborilishi shart!"}, status=status.HTTP_400_BAD_REQUEST)

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            return Response({"error": "Bu username band, boshqasini tanlang"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        return Response({"id": user.id, "username": user.username, "message": "Muvaffaqiyatli ro'yxatdan o'tdingiz!"}, status=status.HTTP_201_CREATED)