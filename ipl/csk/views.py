from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse(<hl>'virat is a captain of rcb'</hl>)
