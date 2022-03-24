import pytest
from django.contrib.auth.models import User

from blog_app.models import Blog


@pytest.fixture
def users():
    users = []
    for x in range(10):
        u = User.objects.create(username=x)
        users.append(u)
    return users


@pytest.fixture
def blogs(users):
    blogs = []
    for user in users:
        for x in range(3):
            b = Blog.objects.create(
                name='x', topic='x', author=user
            )
            blogs.append(b)
    return blogs

@pytest.fixture
def user():
    return User.objects.create(username='bogo')
