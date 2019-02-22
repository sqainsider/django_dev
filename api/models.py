from django.db import models
from movies.models import Movie
from tastypie.resources import ModelResource


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']
