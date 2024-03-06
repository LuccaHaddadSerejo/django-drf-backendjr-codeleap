from django.db import models
from django.utils import timezone


class Codeleap(models.Model):
    class Meta:
        ordering = ["id"]

    username = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    content = models.TextField()
