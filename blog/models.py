from pyexpat import model
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    title  = models.CharField(max_length=200)
    body   = models.TextField()

    def __str__(self):
        return self.title
