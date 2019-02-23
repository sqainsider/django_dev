from django.db import models

# Create your models here.


class Country(models.Model):
    iso_code = models.CharField(max_length=3)
    country = models.CharField(max_length=30)
    currency_code = models.CharField(max_length=3)
    currency = models.CharField(max_length=30)
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.country
