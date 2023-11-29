from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    return HttpResponse('<h1>Welcome</h1>')

def about(request):
    return HttpREsponse('<h1>About us </h1>')

def gallery(request):
    return HttpResponse('<h1> Wow!!</h1>')

    