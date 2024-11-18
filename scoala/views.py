from django.shortcuts import render

# Create your views here.


def scoalaGeneralView(request):
    return render(request, 'scoalaGeneral.html')