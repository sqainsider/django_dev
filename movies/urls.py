from django.urls import path
# from movies import views
from . import views


urlpatterns = [
    path('', views.index, name='movies_index'),
    path('about/', views.about, name='movies_about'),

    path('<int:movie_id>', views.detail, name='movies_detail')
]
