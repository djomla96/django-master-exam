from django.shortcuts import render, get_object_or_404
from .models import Genre, Book

# Create your views here.
def BookList(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.filter(available=True)
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = books.filter(genre=genre)
    return render(request, 'BookSales/book/list.html',
{'genre': genre, 'genres': genres, 'books': books})

def BookDetails(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    return render(request, 'BookSales/book/detail.html', {'book': book})

