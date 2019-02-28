from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    date_created = models.DateTimeField(auto_now_add=True)
