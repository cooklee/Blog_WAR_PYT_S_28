from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    name = models.CharField(max_length=30)
    topic = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # post_set
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_detail_blog", kwargs={'id': self.id})


class Post(models.Model):
    text = models.TextField()
    title = models.TextField(default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text[:20]} {self.creation_date}"

    def get_absolute_url(self):
        return reverse("show_detail_post", kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('update_post', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('delete_post', kwargs={'id': self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    nick = models.CharField(max_length=20)
