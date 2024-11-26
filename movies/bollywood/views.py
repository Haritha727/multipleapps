from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pavankalyan(request):
    return HttpResponse('<h1>pavankalyan is a hero of hollywood</h1>')
