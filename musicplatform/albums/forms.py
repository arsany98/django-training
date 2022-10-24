from dataclasses import field
from django.forms import ModelForm

from .models import Album


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        help_texts = {
            'is_approved': 'Approve the album if its name is not explicit',
        }
