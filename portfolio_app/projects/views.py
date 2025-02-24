from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def projects(request):
    return render(request, 'projects.html')

def single_project(request):
    return render(request, 'single_project.html')