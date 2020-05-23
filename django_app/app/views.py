from django.shortcuts import render, redirect
from .serializers import UserSignupSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .tasks import welcome_registered_user
# Create your views here.


class UserSignupAPIView(CreateAPIView):
    serializer_class = UserSignupSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSignupSerializer

    def perform_create(self, serializer):
        registered_user = serializer.save(self.request)
        welcome_registered_user(registered_user.email, registered_user.username)