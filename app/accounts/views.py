from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username alrady taken.")
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email alrady taken.")
                return redirect(register)
        else:
            messages.error(request, "Passwords do not match")
        return render(request, "accounts/register.html")
    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        return
    else:
        return render(request, "accounts/login.html")


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, "accounts/dashboard.html")
