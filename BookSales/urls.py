from django.urls import path
from . import views

app_name = 'Bookstore'
urlpatterns = [ path('', views.BookList, name='BookList'),
    path('<slug:genre_slug>/', views.BookList, name='BookListByGenre'),
    path('<int:id>/<slug:slug>/', views.BookDetails, name='BookDetails'), ]