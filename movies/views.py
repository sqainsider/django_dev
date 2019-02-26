# movies/views.py

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie


def home(request):
    return HttpResponse("Home Page")


def index(request):

    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

    # movies = Movie.objects.all()i
    # output = ', ' .join([m.title for m in movies])
    # # return HttpResponse("This is index page of movies")
    # return HttpResponse(output)

    # # SELECT * FROM  movies WHERE release date = 1984
    # Movie.objects.fileter(release_date=1984)

    # # select * from movies where id = 1
    # Movie.objects.get(id=1)


def about(request):
    return HttpResponse('Hello from Movies About......')


def detail(request, movie_id):

    # return HttpResponse(movie_id)
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()

    # using [get_object_or_404] instead of try/except
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
