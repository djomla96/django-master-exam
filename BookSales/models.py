from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'genre'
        verbose_name_plural = 'genres'
    def __str__(self): return self.name
    def AbsoluteUrl(self): return reverse('BookSales:BookListByGenre', args=[self.slug])

class Book(models.Model):
    genre = models.ForeignKey(Genre, related_name='books',
    on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    author = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='books/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'books'
    def __str__(self): return self.title
    def AbsoluteUrl(self): return reverse('BookSales:BookDetails', args=[self.id, self.slug])
