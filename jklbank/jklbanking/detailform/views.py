from django.shortcuts import render, redirect
from django.contrib import messages, auth


def detailform(request):
    if request.method == 'POST':
        messages.info(request, 'Appplication accepted')


    return render(request, 'detailform.html')


def logout(request):
    auth.logout(request)
    return redirect('detailform')