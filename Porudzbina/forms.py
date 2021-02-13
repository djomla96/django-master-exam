from django import forms
from .models import Porudzbina

class FormaZaPorudzbinu(forms.ModelForm):
    class Meta:
        model = Porudzbina
        fields = ['ime', 'prezime', 'email', 'adresa',
        'postanski_broj', 'grad'] 