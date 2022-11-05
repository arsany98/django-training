import pytest
from rest_framework.test import APIClient
from ..models import Artist
from ..serializers import ArtistSerializer


def test_create_artist_missing_fields():
    client = APIClient()
    response = client.post('/artists/')
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_artist():
    client = APIClient()
    response = client.post('/artists/', {
        'stage_name': 'Imagine Dragons',
        'social_link': 'https://www.imaginedragonsmusic.com/'
    })
    assert response.status_code == 201

    artist = Artist.objects.all().first()
    assert response.data['stage_name'] == artist.stage_name
    assert response.data['social_link'] == artist.social_link


@pytest.mark.django_db
def test_get_artists():
    Artist.objects.create(stage_name='Imagine Dragons')
    Artist.objects.create(stage_name='Avicii')
    client = APIClient()
    response = client.get('/artists/')
    serializer = ArtistSerializer(Artist.objects.all(), many=True)
    assert response.data == serializer.data
