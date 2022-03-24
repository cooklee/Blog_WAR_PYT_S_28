import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from blog_app.models import Blog, Post


@pytest.mark.django_db
def test_check_index():
    #Client symuluje przeglądarke
    client = Client() # otwieramy nasza przegladarkes
    url = reverse("index") # tworzymy sobie url na
                           # którego chcemy wejsc
    response = client.get(url) # wyejdz na adres url
                               # i wynik wejscia zapisz do
                               # zmiennej response
    assert response.status_code == 200




@pytest.mark.django_db
def test_user_list(users):
    client = Client()
    url = reverse("userlist")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(users)
    for user in users:
        assert user in response.context['object_list']

@pytest.mark.django_db
def test_blog_list(blogs):
    client = Client()
    url = reverse("show_blog")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(blogs)
    for blog in blogs:
        assert blog in response.context['object_list']



@pytest.mark.django_db
def test_check_blog_add_get_not_login():
    client = Client()
    url = reverse("add_blog")
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_blog(user):
    url = reverse('add_blog')
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_blog(user):
    url = reverse('add_blog')
    client = Client()
    client.force_login(user)
    d = {
        'name':'a',
        'topic': 'bb'
    }
    response = client.post(url, d)
    assert response.status_code == 302
    Blog.objects.get(name='a', topic='bb')


@pytest.mark.django_db
def test_register_user():
    url = reverse('register')
    client = Client()
    d = {
        'username':'alamakota',
        'pass1':'aaaaaaaa',
        'pass2': 'aaaaaaaa'
    }
    response = client.post(url, d)
    assert  response.status_code == 302
    User.objects.get(username='alamakota')
    assert client.login(username='alamakota', password='aaaaaaaa')



@pytest.mark.django_db
def test_add_post_with_blog(blogs):
    url = reverse('add_post')
    client = Client()
    d = {
        'text':"manamana",
        'blog':blogs[0].id
    }
    response = client.post(url, d)
    assert Post.objects.first()




