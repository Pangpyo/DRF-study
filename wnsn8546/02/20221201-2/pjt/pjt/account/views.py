from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class Class_name(APIView):
# 	def method_name(self, request, format=None):
#         # 해당 HTTP method를 어떻게 동작시키고 처리할지 개발자가 정의!


