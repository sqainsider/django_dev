# movies/models.py

from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Country(models.Model):
    iso_code = models.CharField(max_length=3)
    country = models.CharField(max_length=30)
    currency_code = models.CharField(max_length=3)
    currency = models.CharField(max_length=30)
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.country


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    # country = models.CharField(max_length=3)
    # language = models.CharField(max_length=30)

    def __str__(self):
        return self.title
