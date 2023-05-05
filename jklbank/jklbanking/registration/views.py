from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= userName, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Enter valid credentials')
            return redirect('login')
    return render(request, 'login.html')