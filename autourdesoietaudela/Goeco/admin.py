from django.contrib import admin
from .models import Composteur
from .models import RecyclerieRessourcerie

# Register your models here.

@admin.register(Composteur)
class ComposteurAdmin(admin.ModelAdmin):
    list_display = ("nom", "entite", "adresse")
    search_fields = ("nom", "entite", "adresse")


@admin.register(RecyclerieRessourcerie)
class RecyclerieRessourcerie(admin.ModelAdmin):
    list_display = ("operateur", "adresse", "code_postal")
    search_fields = ("operateur", "adresse", "code_postal")