from django.forms import BaseInlineFormSet, ModelForm, inlineformset_factory
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django import forms
from .models import Album, Song


class AlbumForm(ModelForm):
    release_datetime = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(
        date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))

    class Meta:
        model = Album
        fields = '__all__'
        help_texts = {
            'is_approved': 'Approve the album if its name is not explicit',
        }


class SongForm(ModelForm):
    name = forms.CharField(required=False)
    audio_file = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'accept': '.mp3, .wav'}),
        validators=[FileExtensionValidator(['mp3', 'wav'])])

    class Meta:
        model = Song
        fields = '__all__'


class SongFormSet(BaseInlineFormSet):
    def clean(self):
        if len(self.deleted_forms) > 0 and len(self.deleted_forms) == len(self.initial_forms):
            raise ValidationError('album must have at leat 1 song')
        return super().clean()
