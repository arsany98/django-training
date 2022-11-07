from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Album
from .serializers import AlbumSerializer
from .permissions import IsArtistOrReadOnly
from django_filters import rest_framework as filters
from .filters import AlbumFilter
from rest_framework.validators import ValidationError


class AlbumListView(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsArtistOrReadOnly]
    queryset = Album.approved_albums.prefetch_related('artist')
    serializer_class = AlbumSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AlbumFilter

    def post(self, request, *args, **kwargs):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['artist'] = request.user.artist
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class AlbumListFiltersView(generics.ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):

        queryset = Album.approved_albums.prefetch_related('artist')
        cost__gte = self.request.query_params.get('cost__gte')
        if cost__gte is not None:
            if not cost__gte.isnumeric():
                raise ValidationError('Enter a number.')
            queryset = queryset.filter(cost__gte=cost__gte)
        cost__lte = self.request.query_params.get('cost__lte')
        if cost__lte is not None:
            if not cost__lte.isnumeric():
                raise ValidationError('Enter a number.')
            queryset = queryset.filter(cost__lte=cost__lte)
        name__icontains = self.request.query_params.get('name')
        if name__icontains is not None:
            queryset = queryset.filter(name__icontains=name__icontains)
        return queryset
