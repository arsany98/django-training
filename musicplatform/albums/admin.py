from django.contrib import admin

from .models import Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fields = ('artist','name', 'creation_datetime', 'release_datetime', 'cost', 'is_approved') 
    readonly_fields = ('creation_datetime',)
    