
from django.db import models
from django.db.models import Count, Q

class ArtistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(approved_albums=Count('album', filter=Q(album__is_approved=True)))
    
class Artist(models.Model):
    objects = ArtistManager()
    stage_name = models.CharField(max_length=50, unique=True)
    social_link = models.URLField(blank=True)

    def approved_albums(self):
        return self.album_set.filter(is_approved=True).count()
    def __str__(self):
        return self.stage_name
    class Meta:
        ordering = ['stage_name']
