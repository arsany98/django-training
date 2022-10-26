from django.shortcuts import render
from django.views.generic import CreateView

from .forms import ArtistForm

from .models import Artist

class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/create.html'