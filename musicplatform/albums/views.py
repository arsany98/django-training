from django.shortcuts import render
from django.views.generic import CreateView

from .forms import AlbumForm

from .models import Album

class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/create.html'
