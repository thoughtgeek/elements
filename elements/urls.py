
#!/usr/bin/env python3

__author__ = "Surya Banerjee"

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from elements.api.views import AppDataViewset


router = DefaultRouter()
router.register(r"appdata", AppDataViewset, basename="appdata")

urlpatterns = [
    path('api/', include(router.urls)),
]
