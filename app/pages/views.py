from django.shortcuts import render

from cars.models import CarsList
from carmanager.models import CarManager
from .cars_Info import vendor_list, models_list, engine_list


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


def search(request):
    query = CarsList.objects.order_by("vendor")

    if "vendor" in request.GET:
        vendor = request.GET["vendor"]
        if vendor:
            query = query.filter(vendor__iexact=vendor)

    if "model" in request.GET:
        model = request.GET["model"]
        if model:
            query = query.filter(model__iexact=model)

    if "engine" in request.GET:
        engine = request.GET["engine"]
        if engine:
            query = query.filter(engine__iexact=engine)

    context = {
        "vendor_list": vendor_list,
        "models_list": models_list,
        "engine_list": engine_list,
        "cars": query,
    }

    return render(request, 'pages/search.html', context)
