from django.urls import path

from .views import AlbumCreateView

urlpatterns = [
    path('create', AlbumCreateView.as_view(), name='album_create')
]
