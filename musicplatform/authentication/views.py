from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from knox import views


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer


class LoginView(views.LoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def get_post_response_data(self, request, token, instance):
        UserSerializer = self.get_user_serializer_class()

        data = {
            'token': token
        }
        if UserSerializer is not None:
            data["user"] = UserSerializer(
                request.user,
                context=self.get_context()
            ).data
        return data

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return super().post(request, format)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
