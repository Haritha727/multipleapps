from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ramcharan(request):
    return HttpResponse('<h1>ramcharan is a globalstar of bollywood</h1>')
