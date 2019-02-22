# movies/admin

from django.contrib import admin
from .models import Genre, Movie, Country


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MoviesGenreAdmin(admin.ModelAdmin):
    # fields = ('id', 'title')
    exclude = ('date_created',)
    list_display = ('id', 'title', 'release_year')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MoviesGenreAdmin)
admin.site.register(Country)
