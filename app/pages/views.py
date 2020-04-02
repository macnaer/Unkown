from django.shortcuts import render

from cars.models import CarsList
from carmanager.models import CarManager


def index(request):

    cars = CarsList.objects.all().filter(is_published=True)[:4]

    context = {
        'cars': cars
    }

    return render(request, 'pages/index.html', context)


def about(request):
    managers = CarManager.objects.all()[:6]

    context = {
        'managers': managers,
    }

    data = {'title': "About Us"}
    return render(request, 'pages/about.html', context)


def services(request):
    data = {'title': "Our Services"}
    return render(request, 'pages/services.html', data)


def contact(request):
    data = {'title': "Contact Us"}
    return render(request, 'pages/contact.html', data)
