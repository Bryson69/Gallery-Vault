from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Gallery

# Create your views here.

def home(request):
    return render(request, 'home.html')

def showcase(request):
    images = Gallery.objects.all()
    return render(request, 'showcase.html', {'images':images})

def show(request, image_id):
    image = Gallery.objects.get(id=image_id)    
    return render(request, 'show.html', {'image':image})
