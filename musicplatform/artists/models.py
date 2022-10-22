from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

class Artist(models.Model):
    stage_name = models.CharField(max_length=50, unique=True)
    social_link = models.URLField(blank=True)
    def __str__(self):
        return self.stage_name
    class Meta:
        ordering = ['stage_name']
