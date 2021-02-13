from django.contrib import admin
from .models import Porudzbina, StavkaPorudzbine

class StavkaPorudzbineInline(admin.TabularInline): 
    model = StavkaPorudzbine
    raw_id_fields = ['book'] 

@admin.register(Porudzbina)
class PorudzbinaAdmin(admin.ModelAdmin):
    list_display = ['id', 'ime', 'prezime', 'email',
    'adresa', 'postanski_broj', 'grad', 'placeno',
    'datum_kreiranja', 'datum_azuriranja']
    list_filter = ['placeno', 'datum_kreiranja', 'datum_azuriranja']
    inlines = [StavkaPorudzbineInline]
