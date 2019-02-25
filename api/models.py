from django.db import models
from movies.models import Movie
from common.models import *
from books.models import *

from tastypie.resources import ModelResource

# API tastypie framework


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']


class CountryResource(ModelResource):
    class Meta:
        queryset = Country.objects.all()
        resource_name = 'countries'
        excludes = ['date_created']


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'books'
        excludes = ['date_created']
