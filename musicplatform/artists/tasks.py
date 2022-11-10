from celery import shared_task
from django.core.mail import send_mass_mail
from django.conf import settings
from .models import Artist
from datetime import timedelta
from django.utils import timezone


@shared_task
def send_inactivity_emails():
    mails_list = []
    for artist in Artist.objects.all():
        recent_albums_count = artist.albums.filter(
            created__gte=timezone.now() - timedelta(days=30)).count()
        if recent_albums_count == 0:
            if artist.user.email == '':
                continue
            subject = 'Inactivity Alert!'
            message = f"""
            Hi {artist.stage_name},

            You are receiving this email because you haven't created an album for a while.
            
            Your inactivity is causing your popularity on our platform to decrease.

            To avoid this, keep creating new albums.

            Regards,
            musicplatform team
            """
            mails_list.append(
                (subject, message, settings.EMAIL_HOST_USER, [artist.user.email]))
    send_mass_mail(mails_list)
