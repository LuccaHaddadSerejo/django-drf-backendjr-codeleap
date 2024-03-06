from django.db import models
from django.utils import timezone


class Codeleap(models.Model):
    class Meta:
        ordering = ["id"]

    username = models.CharField()
    created_datetime = models.DateTimeField(default=timezone.now)
    title = models.CharField()
    content = models.CharField()
