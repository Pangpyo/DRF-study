from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        # id는 django에서 모델 생성할 때 자동으로 생성되는 것
        fields = ('author', 'id', 'title', 'body', 'created_at', 'modified_at')