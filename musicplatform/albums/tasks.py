from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Album


@shared_task
def send_congratulations_email(album_id):
    album = Album.objects.get(pk=album_id)
    artist = album.artist
    if artist.user.email == '':
        return
    message = f"""
    Hi {artist.stage_name},

    Congratulations! You released a new album "{album.name}"
    Can't wait to see what comes next
    
    Regards,
    musicplatform team
    """
    send_mail(subject=f'Congratulations, {artist.stage_name}!',
              message=message,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[artist.user.email])
