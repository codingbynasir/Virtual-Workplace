from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Staff, Bank_statement, Salary_info, User


# Create your views here.

def getLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, username, password)
            return redirect("index")
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")
