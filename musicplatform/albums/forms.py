from django.forms import ModelForm
from django import forms
from .models import Album


class AlbumForm(ModelForm):
    release_datetime = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(
        date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))

    class Meta:
        model = Album
        fields = '__all__'
        help_texts = {
            'is_approved': 'Approve the album if its name is not explicit',
        }
