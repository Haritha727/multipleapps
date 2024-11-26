from django.shortcuts import render

from django.http import HttpResponse
def hari(request):
    return HttpResponse('hari is a intelligent boy')

def junnu(request):
    return HttpResponse('<h1> junnu is good boy </h1>')

def python(request):
    return HttpResponse('<h1><marquee> python is a interpreted </h1></marquee>')
