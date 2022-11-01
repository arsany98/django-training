from django.urls import path

from .views import ArtistCreateView, ArtistListView

urlpatterns = [
    path('create', ArtistCreateView.as_view(), name='artist_create'),
    path('', ArtistListView.as_view(), name='artists')
]
