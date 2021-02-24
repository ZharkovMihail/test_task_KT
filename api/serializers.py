from rest_framework import serializers
from .models import Tag, Picture


class TagSerializer(serializers.ModelSerializer):
    # def to_representation(self, value):
    #     return value.name

    class Meta:
        model = Tag
        fields = ('title',)


class PictureSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Picture
        fields = ('upload', 'tags')
