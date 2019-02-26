from django.urls import path
# from movies import views
from . import views

urlpatterns = [
    path('', views.index, name='splunk_index'),
]
