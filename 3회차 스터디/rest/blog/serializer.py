from .models import Blog, Comment, Like
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    blog = serializers.ReadOnlyField(source="blog.pk")
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Blog
        fields = ['pk', 'title', 'body', 'comments']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    blog = serializers.ReadOnlyField(source="blog.pk")
    class Meta:
        model = Like
        fields = '__all__'