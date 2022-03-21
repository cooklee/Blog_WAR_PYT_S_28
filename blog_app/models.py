from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=30)
    topic = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)


