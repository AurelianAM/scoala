from django.contrib import admin
from .models import FondRate, Incasare, IncasareDiversa, Cheltuiala

# Register your models here.

admin.site.register(FondRate)
admin.site.register(Incasare)
admin.site.register(Cheltuiala)
admin.site.register(IncasareDiversa)