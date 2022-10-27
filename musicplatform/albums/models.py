from email.policy import default
from django.db import models
from model_utils.models import TimeStampedModel


class Album(TimeStampedModel):
    artist = models.ForeignKey(
        'artists.Artist', related_name='albums', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='New Album')
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
