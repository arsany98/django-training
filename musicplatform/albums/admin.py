from django.contrib import admin

from .forms import AlbumForm, SongForm, SongFormSet

from .models import Album, Song


class SongInline(admin.TabularInline):

    model = Song
    fields = ('name', 'image', 'audio_file')
    form = SongForm
    formset = SongFormSet
    min_num = 1
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fields = ('artist', 'name',
              'release_datetime', 'cost', 'is_approved')
    form = AlbumForm
    inlines = (SongInline, )
