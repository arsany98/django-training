import pytest
from rest_framework.test import APIClient
from ..serializers import AlbumSerializer
from ..views import AlbumListView, AlbumListFiltersView


def test_create_album_not_authenticated(album_data):
    client = APIClient()

    response = client.post('/albums/', album_data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_create_album_not_artist(user, auth_client, album_data):
    user1 = user('arsany', 'arsany')
    client = auth_client(user1)
    response = client.post('/albums/', album_data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_create_album_authenticated_artist(user, artist, auth_client, album_data):
    user1 = user('arsany', 'arsany')
    artist1 = artist(stage_name='Imagine Dragons', user=user1)
    client = auth_client(artist1.user)
    response = client.post('/albums/', album_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_album_missing_fields(user, artist, auth_client):
    user1 = user('arsany', 'arsany')
    artist1 = artist(stage_name='Imagine Dragons', user=user1)
    client = auth_client(artist1.user)
    response = client.post('/albums/')
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_albums():
    client = APIClient()
    response = client.get('/albums/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_albums_filter():
    client = APIClient()
    response = client.get('/albums/filter/')
    assert response.status_code == 200


def test_view_serializer():
    v1 = AlbumListView()
    v2 = AlbumListFiltersView()
    assert v1.get_serializer_class() == AlbumSerializer
    assert v2.get_serializer_class() == AlbumSerializer
