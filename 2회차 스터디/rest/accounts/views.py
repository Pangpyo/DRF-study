from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# 기존 장고 방식
def index(request):
    return HttpResponse('index')

# DRF 방식
@api_view()
def index_drf(request):
    return Response({"message": "index"})