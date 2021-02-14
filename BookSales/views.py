from django.shortcuts import render, get_object_or_404
from .models import Genre, Book
from KorpaZaKupovinu.forms import FormaZaDodavanjeKnjigaUKorpu
from KorpaZaKupovinu.korpa import Korpa

# Create your views here.
def BookList(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.filter(available=True)
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = books.filter(genre=genre)
    korpa = Korpa(request)
    return render(request, 'BookSales/book/list.html', 
    {'genre': genre, 'genres': genres, 'books': books, korpa: korpa})

def BookDetails(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    korpa = Korpa(request)
    formazadodavanjeknjigaukorpu = FormaZaDodavanjeKnjigaUKorpu()
    return render(request, 'BookSales/book/detail.html', 
    {'book': book, 'formazadodavanjeknjigaukorpu': formazadodavanjeknjigaukorpu, 'korpa':korpa })

