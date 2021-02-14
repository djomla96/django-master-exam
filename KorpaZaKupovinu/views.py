from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from BookSales.models import Book
from .korpa import Korpa
from .forms import FormaZaDodavanjeKnjigaUKorpu

@require_POST
def DodajUKorpu(request, book_id):
    korpa = Korpa(request)
    book = get_object_or_404(Book, id=book_id)
    form = FormaZaDodavanjeKnjigaUKorpu(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        korpa.Dodaj(book=book, kolicina=cd['kolicina'], dodati_na_kolicinu=cd['dodati_na_kolicinu'])
    return redirect('KorpaZaKupovinu:DetaljiKorpe')

@require_POST
def UkloniIzKorpe(request, book_id):
    korpa = Korpa(request)
    book = get_object_or_404(Book, id=book_id)
    korpa.Ukloni(book)
    return redirect('KorpaZaKupovinu:DetaljiKorpe')

def DetaljiKorpe(request):
    korpa = Korpa(request)
    for stavka in korpa:
        stavka['formazaazuriranjekolicine'] = FormaZaDodavanjeKnjigaUKorpu( initial={'kolicina': 1, 'dodati_na_kolicinu': True})
    return render(request, 'KorpaZaKupovinu/detail.html', {'korpa': korpa})

