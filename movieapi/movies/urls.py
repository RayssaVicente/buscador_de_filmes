from django.urls import path
from . import views

from django.shortcuts import render

def home(request):
    return render(request, 'movies/index.html')  
