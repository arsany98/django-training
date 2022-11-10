import pytest
from users.models import User
from artists.models import Artist
from rest_framework.test import APIClient
import datetime
from django.utils import timezone


@pytest.fixture
def user():
    def inner(*args, **kwargs):
        return User.objects.create_user(*args, **kwargs)
    return inner


@pytest.fixture
def artist():
    def inner(*args, **kwargs):
        return Artist.objects.create(*args, **kwargs)
    return inner


@pytest.fixture
def auth_client():
    client = APIClient()

    def inner(instance=None):
        if instance == None:
            instance = User.objects.create_user(
                username='anonymous', password='anonymous')
        client.force_authenticate(user=instance)
        return client
    return inner


@pytest.fixture
def album_data():
    return {
        'name': 'Evolve',
        'release_datetime': datetime.datetime(
            2017, 6, 23, tzinfo=timezone.get_default_timezone()),
        'cost': '9.49',
    }
