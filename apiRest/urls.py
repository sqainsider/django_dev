from django.urls import path
#from .views import BookAPIView, CountryAPIView, movieAPIView
from .views import *


urlpatterns = [
    path('books/', BookAPIView.as_view(), name='apiRest_books'),
    path('countries/', CountryAPIView.as_view(), name='apiRest_countries'),
    path('movies/', MovieAPIView.as_view(), name='apiRest_movies'),



]
