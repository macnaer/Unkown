from django.shortcuts import render
from django.core.paginator import Paginator

from .models import CarsList


def index(request):
    carlist = CarsList.objects.all().filter(is_published=True)

    paginator = Paginator(carlist, 1)
    page = request.GET.get("page")
    paged_carlist = paginator.get_page(page)

    context = {
        "carlist": paged_carlist
    }

    return render(request, "carlist/carlist.html", context)


def singlecar(request):
    return render(request, "carlist/carlist.html")
