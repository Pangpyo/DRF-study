from .models import TODO
from rest_framework import serializers


class TODOserializers(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = "__all__"
