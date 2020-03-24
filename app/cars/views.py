from django.shortcuts import render


def index(request):
    data = {
        'title': 'Car listing'
    }
    return render(request, "carlist/carlist.html", data)


def singlecar(request):
    return render(request, "carlist/carlist.html")
