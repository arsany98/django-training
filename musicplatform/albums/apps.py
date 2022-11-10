from django.apps import AppConfig
from django.db.models.signals import post_save


class AlbumsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'albums'

    def ready(self):
        from .signals import send_email
        return super().ready()
