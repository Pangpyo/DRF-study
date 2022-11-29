from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            nickname=validated_data["nickname"],
            password=validated_data["password"],
        )
        return user

    class Meta:
        model = User
        fields = ["email", "nickname", "password"]
