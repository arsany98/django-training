from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Album
from .tasks import send_congratulations_email
from .serializers import AlbumSerializer


@receiver(post_save, sender=Album)
def send_email(sender, **kwargs):
    send_congratulations_email.delay(kwargs['instance'].id)
