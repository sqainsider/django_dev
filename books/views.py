from django.shortcuts import render

from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

# Create your views here.
