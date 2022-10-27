from django.contrib import admin

from .forms import AlbumForm

from .models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fields = ('artist', 'name', 
              'release_datetime', 'cost', 'is_approved')
    form = AlbumForm
