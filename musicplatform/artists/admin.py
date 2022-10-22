from django.contrib import admin

from albums.models import Album

from .models import Artist

class AlbumsInline(admin.TabularInline):
    model = Album
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'get_num_of_approved_albums')
    inlines = (AlbumsInline,)
