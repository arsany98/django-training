from email.policy import default
from django.db import models

class Album(models.Model):
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='New Album')
    creation_datetime = models.DateTimeField()
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    def __str__(self):
        return self.name