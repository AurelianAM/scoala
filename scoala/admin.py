from django.contrib import admin
from .models import Profesor, Clasa, Elev, AnScolar

# Register your models here.

admin.site.register(Profesor)
admin.site.register(Clasa)
admin.site.register(Elev)
admin.site.register(AnScolar)