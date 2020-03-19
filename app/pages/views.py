from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    data = {'title': "About Us"}
    return render(request, 'pages/about.html', data)


def services(request):
    data = {'title': "Our Services"}
    return render(request, 'pages/services.html', data)


def contact(request):
    data = {'title': "Contact Us"}
    return render(request, 'pages/contact.html', data)
