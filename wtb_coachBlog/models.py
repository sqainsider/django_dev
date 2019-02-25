from django.db import models

from django.contrib.auth.models import User


class CoachPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User',
                               on_delete=models.CASCADE),

    def __str__(self):
        return self.title
