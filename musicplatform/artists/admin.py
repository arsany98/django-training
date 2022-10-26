from django.contrib import admin

from albums.models import Album
from albums.forms import AlbumForm

from .models import Artist

class AlbumsInline(admin.TabularInline):
    model = Album
    fields = ('artist', 'name',
              'release_datetime', 'cost', 'is_approved')
    form = AlbumForm
    extra = 1
    
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'approved_albums')
    inlines = (AlbumsInline,)
