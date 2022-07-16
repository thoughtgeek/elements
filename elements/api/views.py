#!/usr/bin/env python3

__author__ = "Surya Banerjee"

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from elements.api.models import AppData
from elements.api.serializers import AppDataDetailSerializer, AppDataListSerializer


class AppDataViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = AppDataListSerializer
    detail_serializer = AppDataDetailSerializer
    queryset = AppData.objects.all()

    http_method_names = ["get"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            if hasattr(self, "detail_serializer"):
                return self.detail_serializer
        return super(AppDataViewset, self).get_serializer_class()
