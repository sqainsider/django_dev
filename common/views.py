from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, Http404


def home(request):
    # return HttpResponse("Home Page..........")
    return render(request, 'home.html')


mission = 'This is mission'


def about(request):
    # return HttpResponse('Hello from Home About......')
    return render(request, 'about.html')

    # return render(request, 'movies/detail.html', {'movie': movie})
