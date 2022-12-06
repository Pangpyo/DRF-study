from .models import Blog,Comment
from rest_framework import serializers



class BlogSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source = 'user.nickname')
    image = serializers.ImageField(use_url=True)
    is_like = serializers.SerializerMethodField("is_like_field")

    def is_like_field(self, blog):
        if "request" in self.context:
            user = self.context["request"].user
            return blog.like_user_set.filter(pk=user.pk).exists()
        return False


    class Meta:
        model = Blog
        fields = ['id', 'title', 'created_at', 'user', 'body','image','is_like']
    

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Comment
        fields = ['id', 'blog', 'user', 'created_at', 'comment']
