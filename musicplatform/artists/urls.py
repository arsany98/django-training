from django.urls import path

from .views import ArtistCreateView

urlpatterns = [
    path('create', ArtistCreateView.as_view())
]
