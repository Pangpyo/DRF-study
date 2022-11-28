from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# 기존 django 방식
# HttpResponse는 django 기능
def hello_world(request):
    return HttpResponse('Hello_world!')

# DRF 방식
# django과 다르게 Response를 사용
@api_view()
def hello_world_drf(request):
    return Response({'message': 'Hello_world'})