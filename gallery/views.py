from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def showcase(request):
    return render(request, 'showcase.html')

def show(request):
    return render(request, 'show.html')
