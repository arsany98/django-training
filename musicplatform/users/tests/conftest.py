import pytest
from rest_framework.test import APIClient
from users.models import User


@pytest.fixture
def user():
    def inner(username, password):
        return User.objects.create_user(
            username=username, password=password)
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
