from rest_framework import serializers

from core.models import Advertisement, Tag
from django.conf import settings


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serialize an ad"""
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'caption', 'image', 'tags')
        read_only_fields = ('id',)


class TagSerializer(serializers.ModelSerializer):
    """Serialize a tag"""

    class Meta:
        model = Tag
        fields = ('title',)


class AdvertisementDetailedSerializer(AdvertisementSerializer):
    tags = TagSerializer(many=True, read_only=True)