from rest_framework import serializers
from .models import Board, Comment

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        # id는 django에서 모델 생성할 때 자동으로 생성되는 것
        fields = ('author', 'id', 'title', 'body', 'created_at', 'modified_at')

class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('board', 'id', 'user', 'parent', 'comment', 'created_at','reply')
        read_only_fields = ['user']

    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data