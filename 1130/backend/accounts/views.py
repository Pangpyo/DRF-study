from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
