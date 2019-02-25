from django.urls import path
from .views import BookAPIView

urlpatterns = [
    path('rest/books', BookAPIView.as_view(), name='api_books'),


]
