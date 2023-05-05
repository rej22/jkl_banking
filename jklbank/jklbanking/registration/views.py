from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


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


def register(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']
        confirmPswd = request.POST['confirm_pswd']

        if password == confirmPswd:
            user = User.objects.create_user(username=userName, password=password)
            user.save()
            return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')