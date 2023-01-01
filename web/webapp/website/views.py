from django.shortcuts import render
from django.http import HttpResponse

def teszt(request):
    return HttpResponse("Hello world!")
