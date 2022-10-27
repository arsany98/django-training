from django.urls import path

from .views import ArtistCreateView, ArtistListView

urlpatterns = [
    path('create', ArtistCreateView.as_view()),
    path('', ArtistListView.as_view())
]
