from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def alluarjun(request):
    return HttpResponse('<h1>alluarjun is a hero tollywood</h1>')

def ramcharan(request):
    return HttpResponse('<hl>ramcharan is a globalstar bollywood</h1')
