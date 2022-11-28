from .serializers import ArticleSerializer
from rest_framework import viewsets
from .models import Article


# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
