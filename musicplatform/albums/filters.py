from django_filters import rest_framework as filters
from .models import Album


class AlbumFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'icontains')
    cost__gte = filters.NumberFilter('cost', 'gte')
    cost__lte = filters.NumberFilter('cost', 'lte')

    class Meta:
        model = Album
        fields = ('name', 'cost')
