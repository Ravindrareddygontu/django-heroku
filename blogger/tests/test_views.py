import pytest
from django import urls
from blogger.models import Blog
from django.contrib.auth.forms import get_user_model


@pytest.mark.django_db
@pytest.mark.parametrize('url', [('home'), ('signup'), ('login'), ('dashboard')])
def test_urls(client, url):
    temp_url = urls.reverse(url)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_models():
    title = Blog.objects.create(Title='education')
    assert str(title) == 'education'


@pytest.mark.django_db
def test_user_signup(client, signup_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    signup_url = urls.reverse('signup')
    resp = client.post(signup_url, signup_data)
    assert user_model.objects.count() == 1
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_login(client, login_data, signup_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('login')
    resp = client.post(login_url, data=signup_data)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('base')


@pytest.mark.django_db
def test_user_logout(client):
    logout_url = urls.reverse('logout')
    resp = client.get(logout_url)
    assert resp.status_code == 200



