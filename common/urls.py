
from django.urls import path
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

]
