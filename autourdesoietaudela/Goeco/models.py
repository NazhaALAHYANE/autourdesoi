from django.db import models

# Create your models here.

class Composteur(models.Model):
    nom= models.CharField(max_length=200, verbose_name="Nom du site")
    entite= models.CharField(max_length=200, verbose_name="Entité en charge")
    adresse= models.CharField(max_length=300, verbose_name="Adresse")
    arrondissement= models.CharField(max_length=10, blank=True, null=True, verbose_name="Arrodissement")

    def __str__(self):
        return self.nom