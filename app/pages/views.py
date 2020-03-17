from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        "title": "Welcome",
        "subtitle": "This is a best site for a simple marketing or informational website. It includes a large callout called a jumbotron and three supporting pieces of content. Use it as a starting point to create something more unique."
    }
    return render(request, 'pages/index.html', data)


def about(request):
    return render(request, 'pages/about.html')
