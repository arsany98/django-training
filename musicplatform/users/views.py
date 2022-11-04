from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from .models import User


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, )
