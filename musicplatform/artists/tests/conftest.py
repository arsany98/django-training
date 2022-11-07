import pytest
from users.models import User
from artists.models import Artist


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
