from typing import Any
from django.db import models
from django.db.models import signals
from datetime import datetime

# Create your models here.

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nume} {self.prenume}"

class Clasa(models.Model):
    id = models.AutoField(primary_key=True)
    an = models.IntegerField()
    anStart = models.IntegerField()
    litera = models.CharField(max_length=1)
    fond = models.DecimalField( max_digits=7, decimal_places=2, default=0)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.an} {self.litera} - {self.profesor}"

class Elev(models.Model):
    id = models.AutoField(primary_key=True)
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=100)
    contributie = models.DecimalField( max_digits=7, decimal_places=2, default=0)
    restDePlata = models.DecimalField( max_digits=7, decimal_places=2, default=0)
    clasa = models.ForeignKey(Clasa, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nume} | {self.prenume} | {self.contributie} lei | {self.restDePlata} lei | {self.clasa}"

class AnScolar(models.Model):
    id = models.AutoField(primary_key=True)
    anStart = models.IntegerField(default=datetime.now().year)
    anFinal = models.IntegerField(default=datetime.now().year + 1)

    def __str__(self):
        return f"Anul {self.anStart} - {self.anFinal}"
    
def anScolarAfterSave(sender, instance, created, **kwargs):
    if created:
        toateClasele = Clasa.objects.all()
        for clasa in toateClasele:
            clasa.an = instance.anStart - clasa.anStart
            clasa.save()

signals.post_save.connect(anScolarAfterSave, sender=AnScolar)