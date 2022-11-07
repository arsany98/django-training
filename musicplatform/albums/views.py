from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Album
from .serializers import AlbumSerializer
from .permissions import IsArtistOrReadOnly


class AlbumListView(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsArtistOrReadOnly]
    queryset = Album.approved_albums.prefetch_related('artist')
    serializer_class = AlbumSerializer

    def post(self, request, *args, **kwargs):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['artist'] = request.user.artist
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
