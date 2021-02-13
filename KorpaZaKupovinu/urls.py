from django.urls import path
from . import views

app_name = 'korpazakupovinu'
urlpatterns = [
    path('', views.DetaljiKorpe, name='DetaljiKorpe'),
    path('dodaj/<int:book_id>/', views.DodajUKorpu, name='DodajUKorpu'),
    path('ukloni/<int:book_id>/', views.UkloniIzKorpe, name='UkloniIzKorpe'),
] 