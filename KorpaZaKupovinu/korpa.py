from decimal import Decimal
from django.conf import settings
from BookSales.models import Book

class Korpa(object):
    def __init__(self, request):
        self.sesija = request.session
        korpa = self.sesija.get(settings.KORPA_ZA_KUPOVINU_SESSION_KEY)
        
        if not korpa:
            korpa = self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY] = {}
        self.korpa = korpa
    
    def __iter__(self):
        book_ids = self.korpa.keys()
        books = Book.objects.filter(id__in=book_ids)
        korpakopija = self.korpa.copy()
        for book in books:
            korpakopija[str(book.id)]['book'] = book
        for stavka in korpakopija.values():
            stavka['price'] = Decimal(stavka['price'])
            stavka['ukupna_price'] = stavka['price'] * stavka['kolicina']
            yield stavka
    
    def __len__(self):
        return sum(stavka['kolicina'] for stavka in self.korpa.values()) 

    def Dodaj(self, book, kolicina=1, dodati_na_kolicinu=True):
        book_id = str(book.id)
        if book_id not in self.korpa:
            self.korpa[book_id] = {'kolicina': 0, 'price': str(book.price)}
        if dodati_na_kolicinu: self.korpa[book_id]['kolicina'] += kolicina
        else: self.korpa[book_id]['kolicina'] = kolicina
        self.sesija.modified = True
    
    def Ukloni(self, book):
        book_id = str(book.id)
        if book_id in self.korpa:
            del self.korpa[book_id]
            self.sesija.modified = True
    
    def ObrisiJeIzSesije(self):
        del self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY]
        self.sesija.modified = True

    def UzmiUkupnuCenu(self):
        return sum(Decimal(stavka['price']) * stavka['kolicina'] for stavka in
        self.korpa.values())
