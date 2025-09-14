from django.contrib import admin
from .models import Composteur

# Register your models here.

@admin.register(Composteur)
class ComposteurAdmin(admin.ModelAdmin):
    list_display = ("nom", "entite", "adresse")
    search_fields = ("nom", "entite", "adresse")
