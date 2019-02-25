from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    due_date = models.DateTimeField()
    date_created = models.DateTimeField(
        default=timezone.now)
    date_updated = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title
