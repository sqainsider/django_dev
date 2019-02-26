from django.urls import path
from .views import BookAPIView

urlpatterns = [
    path('movies/', BookAPIView.as_view(), name='api_books'),


]
