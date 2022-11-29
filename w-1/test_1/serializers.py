from .models import Articles
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"
