from django.shortcuts import render
from scoala.models import Clasa

# Create your views here.

def homeView(request):
    context = {}
    if request.method == "GET":
        toateClasele = Clasa.objects.all()
        context.update({'toateClasele' : toateClasele})
    
    return render(request, 'home.html', context=context)