from django.urls import path
from . import views

app_name = 'porudzbine'

urlpatterns = [ 
    path('kreirajporudzbinu/',  views.KreiranjePorudzbine, name='KreiranjePorudzbine'), ]
