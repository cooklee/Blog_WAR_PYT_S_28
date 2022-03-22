from django.db import models

# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    name = models.CharField(max_length=30)
    topic = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)

    # post_set
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_detail_blog", kwargs={'id': self.id})


class Post(models.Model):
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text[:20]} {self.creation_date}"

    def get_absolute_url(self):
        return reverse("show_detail_post", kwargs={'id': self.id})
