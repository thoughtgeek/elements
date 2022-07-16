from django.db import models

class AppData(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.TextField()
