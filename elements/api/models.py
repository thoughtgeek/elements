#!/usr/bin/env python3

__author__ = "Surya Banerjee"

from django.db import models
from cacheops import invalidate_model

class AppData(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.TextField()

    def save(self, *args, **kwargs):
        super(AppData, self).save(*args, **kwargs)
        invalidate_model(AppData)

    def __str__(self):
        return f"id:{self.id}, title:{self.title}"
