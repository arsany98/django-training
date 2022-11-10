
from django.db import models
from django.db.models import Count, Q
from django.conf import settings


class ArtistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(approved_albums=Count('albums', filter=Q(albums__is_approved=True)))


class Artist(models.Model):
    objects = ArtistManager()
    stage_name = models.CharField(max_length=50, unique=True)
    social_link = models.URLField(blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def approved_albums(self):
        return self.albums.filter(is_approved=True).count()

    def __str__(self):
        return self.stage_name

    class Meta:
        ordering = ['stage_name']
