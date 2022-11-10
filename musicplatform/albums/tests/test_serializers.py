from ..serializers import AlbumSerializer
from ..models import Album
import pytest


@pytest.mark.django_db
def test_serialization(user, artist, album_data):
    user1 = user('arsany', 'arsany')
    artist1 = artist(stage_name='Imagine Dragons', user=user1)

    album = Album.objects.create(artist=artist1,
                                 **album_data)

    serializer = AlbumSerializer(album)

    assert serializer.data.keys() == {
        'id', 'name', 'release_datetime', 'cost', 'artist'
    }
    assert serializer.data['id'] == album.id
    assert serializer.data['name'] == album.name
    assert serializer.data['release_datetime'] == album.release_datetime.isoformat(
    )
    assert serializer.data['cost'] == str(album.cost)

    assert serializer.data['artist']['id'] == album.artist.id
    assert serializer.data['artist']['stage_name'] == album.artist.stage_name
    assert serializer.data['artist']['social_link'] == album.artist.social_link
    assert serializer.data['artist']['user'] == album.artist.user.id


@pytest.mark.django_db
def test_deserialization(user, artist, album_data):
    user1 = user('arsany', 'arsany')
    artist1 = artist(stage_name='Imagine Dragons', user=user1)
    serializer = AlbumSerializer(data=album_data, context={'artist': artist1})
    assert serializer.is_valid() == True

    created_album = serializer.create(serializer.validated_data)
    assert album_data['name'] == created_album.name
    assert album_data['release_datetime'] == created_album.release_datetime
    assert album_data['cost'] == str(created_album.cost)
