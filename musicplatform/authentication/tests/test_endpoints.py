import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


def test_registration_missing_fields():
    client = APIClient()
    response = client.post('/authentication/register/')
    assert response.status_code == 400


@pytest.mark.django_db
def test_register():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'test',
        'email': '',
        'password': 'test3957',
        'confirm_password': 'test3957'
    })
    assert response.status_code == 201

    user = get_user_model().objects.all().first()
    assert response.data['username'] == user.username
    assert response.data['email'] == user.email


def test_login_missing_fields():
    client = APIClient()
    response = client.post('/authentication/login/')
    assert response.status_code == 400


@pytest.mark.django_db
def test_login(user):
    user1 = user('test', 'test')
    client = APIClient()
    response = client.post('/authentication/login/', {
        'username': 'test',
        'password': 'test'
    })
    assert response.status_code == 200
    assert response.data['token']
    assert response.data['user']['id'] == user1.id
    assert response.data['user']['username'] == user1.username
    assert response.data['user']['email'] == user1.email
    assert response.data['user']['bio'] == user1.bio
