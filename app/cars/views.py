from django.shortcuts import render

from .models import CarsList


def index(request):
    carlist = CarsList.objects.all()

    context = {
        "carlist": carlist
    }

    return render(request, "carlist/carlist.html", context)


def singlecar(request):
    return render(request, "carlist/carlist.html")
