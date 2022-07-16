#!/usr/bin/env python3

__author__ = "Surya Banerjee"


from rest_framework import serializers
from elements.api.models import AppData


class AppDataListSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    # Truncate if too long
    def get_title(self, obj):
        return (obj.title[:28] + '...') if len(obj.title) > 28 else obj.title

    class Meta:
        model = AppData
        fields = ["id", "title"]


class AppDataDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppData
        fields = ["id", "title", "description", "image"]
