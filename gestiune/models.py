from typing import Any
from django.db import models
from scoala.models import AnScolar, Clasa, Elev

# Create your models here.


class FondRate(models.Model):
    id = models.AutoField(primary_key=True)
    anScolar = models.ForeignKey(AnScolar, on_delete=models.CASCADE, null=False)
    clasa = models.ForeignKey(Clasa, on_delete=models.CASCADE, null=False)
    suma = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_applied = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Fonduri de rate"

    def __str__(self):
        return f'{self.anScolar} {self.clasa} {self.suma}lei'

class Incasare(models.Model):
    id = models.AutoField(primary_key=True)
    elev = models.ForeignKey(Elev, on_delete=models.SET_NULL, null=True)
    suma = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now=True)
    is_applied = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Incasari"

    def __str__(self):
        return f'{self.elev.nume} {self.elev.prenume} a platit {self.suma} lei procesat = {self.is_applied}'

class IncasareDiversa(models.Model):
    id = models.AutoField(primary_key=True)
    clasa = models.ForeignKey(Clasa, on_delete=models.SET_NULL, null=True)
    suma = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    detalii = models.TextField()
    created = models.DateTimeField(auto_now=True)
    is_applied = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Incasari Diverse"

    def __str__(self):
        return f'{self.created} - {self.suma} lei - {self.detalii} = {self.is_applied}'

class Cheltuiala(models.Model):
    id = models.AutoField(primary_key=True)
    clasa = models.ForeignKey(Clasa, on_delete=models.SET_NULL, null=True)
    suma = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    detalii = models.TextField()
    created = models.DateTimeField(auto_now=True)
    is_applied = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Cheltuieli Diverse"

    def __str__(self):
        return f'{self.created} - {self.suma} lei - {self.detalii} = {self.is_applied}'

def fondRateAfterSave(sender, instance, created, **kwargs):
    if instance.is_active and not instance.is_applied:
        totiElevii = Elev.objects.filter(clasa = instance.clasa)
        if totiElevii is not None:
            for elev in totiElevii:
                elev.restDePlata += instance.suma
                elev.save()
        instance.is_applied = True
        instance.save()

def fondRateAfterDelete(sender, instance, **kwargs):
    if instance.is_active and instance.is_applied:
        totiElevii = Elev.objects.filter(clasa = instance.clasa)
        if totiElevii is not None:
            for elev in totiElevii:
                elev.restDePlata -= instance.suma
                elev.save()

def incasareAfterSave(sender, instance, created, **kwargs):
    if not instance.is_applied:
        elev = instance.elev
        clasa = elev.clasa
        elev.restDePlata -= instance.suma
        elev.contributie += instance.suma
        clasa.fond += instance.suma
        elev.save()
        clasa.save()
        instance.is_applied = True
        instance.save()

def incasareAfterDelete(sender, instance, **kwargs):
    if instance.is_applied:
        elev = instance.elev
        clasa = elev.clasa
        clasa.fond -= instance.suma
        clasa.save()
        elev.restDePlata += instance.suma
        elev.contributie -= instance.suma
        elev.save()

def cheltuialaAfterSave(sender, instance, created, **kwargs):
    if not instance.is_applied:
        clasa = instance.clasa
        clasa.fond -= instance.suma
        clasa.save()
        instance.is_applied = True
        instance.save()

def cheltuialaAfterDelete(sender, instance, **kwargs):
    if instance.is_applied:
        clasa = instance.clasa
        clasa.fond += instance.suma
        clasa.save()

def incasareDiversaAfterSave(sender, instance, created, **kwargs):
    if not instance.is_applied:
        clasa = instance.clasa
        clasa.fond += instance.suma
        clasa.save()
        instance.is_applied = True
        instance.save()


def incasareDiversaAfterDelete(sender, instance, **kwargs):
    if instance.is_applied:
        clasa = instance.clasa
        clasa.fond -= instance.suma
        clasa.save()

models.signals.post_save.connect(fondRateAfterSave, sender=FondRate)
models.signals.post_delete.connect(fondRateAfterDelete, sender=FondRate)

models.signals.post_save.connect(incasareAfterSave, sender=Incasare)
models.signals.post_delete.connect(incasareAfterDelete, sender=Incasare)

models.signals.post_save.connect(cheltuialaAfterSave, sender=Cheltuiala)
models.signals.post_delete.connect(cheltuialaAfterDelete, sender=Cheltuiala)

models.signals.post_save.connect(incasareDiversaAfterSave, sender=IncasareDiversa)
models.signals.post_delete.connect(incasareDiversaAfterDelete, sender=IncasareDiversa)