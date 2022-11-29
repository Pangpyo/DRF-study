from django.shortcuts import render
from .models import Articles
from .serializers import ArticleSerializer
from rest_framework import viewsets

# Create your views here.


class ArticlesViewset(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
