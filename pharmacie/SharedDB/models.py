from django.db import models

# Create your models here.
class acheteur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=10)
    prenom = models.CharField(max_length=30)
    age = models.IntegerField()
    CIN = models.CharField(max_length=13)
    class meta:
        app_label='SharedDB'

class pharmacien(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    sexe  = models.CharField(max_length=1)
    address = models.CharField(max_length=100)
    salaire = models.IntegerField()
    class meta:
        app_label='SharedDB'

class medicament(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    code = models.CharField(max_length=10)    
    prix = models.IntegerField()
    description = models.CharField(max_length=255)
    dateExpiration = models.DateField()
    stockDisponible = models.IntegerField()
    class meta:
        app_label='SharedDB'
