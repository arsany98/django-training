import pytest
from rest_framework.test import APIClient
from ..models import Artist
from ..serializers import ArtistSerializer


def test_create_artist_missing_fields():
    client = APIClient()
    response = client.post('/artists/')
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_artist(user):
    client = APIClient()

    user1 = user('arsany', 'arsany')
    response = client.post('/artists/', {
        'stage_name': 'Imagine Dragons',
        'social_link': 'https://www.imaginedragonsmusic.com/',
        'user': user1.id
    })
    assert response.status_code == 201

    artist = Artist.objects.all().first()
    assert response.data['stage_name'] == artist.stage_name
    assert response.data['social_link'] == artist.social_link
    assert response.data['user'] == artist.user.id


@pytest.mark.django_db
def test_get_artists(user, artist):
    client = APIClient()

    user1 = user('arsany', 'arsany')
    artist(stage_name='Imagine Dragons', user=user1)
    user2 = user('test', 'test')
    artist(stage_name='Avicii', user=user2)

    response = client.get('/artists/')
    serializer = ArtistSerializer(Artist.objects.all(), many=True)

    assert response.data['results'] == serializer.data
