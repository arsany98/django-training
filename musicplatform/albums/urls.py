from django.urls import path
from .views import AlbumListView, AlbumListFiltersView
urlpatterns = [
    path('', AlbumListView.as_view()),
    path('filter/', AlbumListFiltersView.as_view()),
]
