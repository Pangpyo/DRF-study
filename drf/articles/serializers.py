from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Article
        fields = (
            "pk",
            "title",
            "content",
            "user",
        )
