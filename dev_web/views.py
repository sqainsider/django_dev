# movies/views.py

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404


def home(request):
    # return HttpResponse("SQAInsider Home Page")
    # return render(request, 'movies/index.html', {'movies': movies})
    return render(request, 'movies/index.html', )

    # return render(request, 'home.html', )
