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
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email alrady taken.")
                    return redirect(register)
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password, first_name=first_name, last_name=last_name,)
                    user.save()
                    messages.success(request, "You are registred. Log in")
                    return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
        return redirect('register')
    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Login or password incorrect")
            return redirect('login')
    else:
        return render(request, "accounts/login.html")


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, "accounts/dashboard.html")
