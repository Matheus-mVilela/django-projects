from django.shortcuts import render, redirect
from django.contrib.auth import logout


def homepage(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect('homepage')
