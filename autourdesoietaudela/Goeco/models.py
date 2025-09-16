from django.db import models

# Create your models here.

class Composteur(models.Model):
    nom= models.CharField(max_length=200, verbose_name="Nom du site")
    entite= models.CharField(max_length=200, verbose_name="Entité en charge")
    adresse= models.CharField(max_length=300, verbose_name="Adresse")
    arrondissement= models.CharField(max_length=10, blank=True, null=True, verbose_name="Arrodissement")

    def __str__(self):
        return self.nom

class RecyclerieRessourcerie(models.Model):
    operateur= models.CharField(max_length=255, verbose_name="Opérateur")
    adresse= models.CharField(max_length=255, verbose_name="Adresse")
    code_postal= models.CharField(max_length=10, verbose_name="Code postal")

    class Meta:
        verbose_name= "Recyclerie/ Ressourcerie/ Point d'apport volontaire"
        verbose_name_plural= "Recycleries/ Ressourceries/ Points d'apport volontaire"
    
    def __str__(self):
        return f"{self.operateur} - {self.adresse} ({self.code_postal})"