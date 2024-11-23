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

    def __str__(self):
        return f'{self.anScolar} {self.clasa} {self.suma}lei'

class Incasare(models.Model):
    id = models.AutoField(primary_key=True)
    elev = models.ForeignKey(Elev, on_delete=models.SET_NULL, null=True)
    suma = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now=True)
    is_applied = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.elev.nume} {self.elev.prenume} a platit {self.suma} lei procesat = {self.is_applied}'

def fondRateAfterSave(sender, instance, created, **kwargs):
    if instance.is_active and not instance.is_applied:
        totiElevii = Elev.objects.filter(clasa = instance.clasa)
        if totiElevii is not None:
            for elev in totiElevii:
                elev.restDePlata += instance.suma
                elev.save()
        instance.is_applied = True
        instance.save()

def incasareAfterSave(sender, instance, created, **kwargs):
    if not instance.is_applied:
        elev = instance.elev
        elev.restDePlata -= instance.suma
        elev.contributie += instance.suma
        elev.save()
        instance.is_applied = True
        instance.save()

models.signals.post_save.connect(fondRateAfterSave, sender=FondRate)
models.signals.post_save.connect(incasareAfterSave, sender=Incasare)