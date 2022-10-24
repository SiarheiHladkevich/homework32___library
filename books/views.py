from django.shortcuts import render
from .models import *

# Create your views here.
def books_list(request):
    books = Book.objects.all().order_by('title')
    authors = Author.objects.all()
    genres = Genre.objects.all()
    context = {
        'books': books,
        'authors': authors,
        'genres': genres
    }
    return render(request, 'index.html', context)

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'book_detail.html', context)
