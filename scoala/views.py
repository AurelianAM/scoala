from django.shortcuts import render
from .models import Clasa, Elev

# Create your views here.


def scoalaGeneralView(request):
    context = {}
    if request.method == "GET":
        toateClasele = Clasa.objects.all()
        context.update({'toateClasele' : toateClasele})
    elif request.method == "POST":
        idClasa = request.POST.get("clasa")
        clasa = Clasa.objects.get(id = idClasa)
        eleviDinClasa = Elev.objects.filter(clasa = int(idClasa))
        context.update({'eleviDinClasa' : eleviDinClasa, 'clasa':clasa})
        return render(request, 'eleviClasa.html', context=context)
    
    return render(request, 'scoalaGeneral.html', context=context)