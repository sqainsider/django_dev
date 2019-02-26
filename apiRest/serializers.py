#


from rest_framework import serializers

from books.models import Book
from movies.models import Movie
from common.models import Country


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('iso_code', 'country', 'currency_code',
                  'currency', 'language')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'release_year', 'number_in_stock',
                  'daily_rate', 'genre', 'country')
