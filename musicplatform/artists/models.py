from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

class Artist(models.Model):
    stage_name = models.CharField(max_length=50, unique=True)
    social_link = models.URLField(blank=True)
    class Meta:
        ordering = ['stage_name']
