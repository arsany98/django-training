import pytest
from rest_framework.test import APIClient
from ..models import User


@pytest.mark.django_db
def test_is_owner_permission_not_owner(user, auth_client):
    user1 = user('arsany', 'arsany')

    client = auth_client()
    response = client.put(f'/users/{user1.id}/',
                          {'username': 'test', 'bio': 'hello'})
    assert response.status_code == 403

    response = client.patch(f'/users/{user1.id}/', {'username': 'test'})
    assert response.status_code == 403


@pytest.mark.django_db
def test_is_owner_permission_owner(user, auth_client):
    user1 = user('arsany', 'arsany')

    client = auth_client(user1)
    response = client.put(f'/users/{user1.id}/',
                          {'username': 'test', 'bio': 'hello'})
    assert response.status_code == 200

    response = client.patch(f'/users/{user1.id}/', {'bio': 'hi'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_user(user, auth_client):
    user1 = user('arsany', 'arsany')
    client = auth_client(user1)

    response = client.put(f'/users/{user1.id}/',
                          {'username': 'test', 'bio': 'hello'})
    updated_user = User.objects.get(pk=user1.id)
    assert response.data['username'] == updated_user.username
    assert response.data['bio'] == updated_user.bio

    response = client.patch(f'/users/{user1.id}/', {'bio': 'hi'})
    updated_user = User.objects.get(pk=user1.id)
    assert response.data['bio'] == updated_user.bio


@pytest.mark.django_db
def test_get_user(user):
    user1 = user('arsany', 'arsany')
    user1.email = 'arsany@maged.com'
    user1.bio = 'hello'
    user1.save()
    client = APIClient()
    response = client.get(f'/users/{user1.id}/')
    assert response.status_code == 200

    assert response.data['id'] == user1.id
    assert response.data['username'] == user1.username
    assert response.data['email'] == user1.email
    assert response.data['bio'] == user1.bio
