from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import ArtistForm

from .models import Artist


class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/create.html'


class ArtistListView(ListView):
    queryset = Artist.objects.prefetch_related('albums')
    template_name = 'artists/list.html'
