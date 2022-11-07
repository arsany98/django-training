from django.db import models
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class AlbumManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)


class Album(TimeStampedModel):
    objects = models.Manager()
    approved_albums = AlbumManager()
    artist = models.ForeignKey(
        'artists.Artist', related_name='albums', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='New Album')
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(
        Album, related_name='songs', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='song_images')
    image_thumbnail = ImageSpecField(
        processors=[ResizeToFill(50, 50)], format='JPEG', options={'quality': 60}, source='image')
    audio_file = models.FileField(upload_to='songs')

    def __str__(self):
        return self.name

    def save(self):
        if not self.name:
            self.name = self.album.name
        return super().save()
