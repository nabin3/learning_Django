from django.http import HttpResponse
from django.shortcuts import render

def home(request): # this method must be named as home
    # return HttpResponse("<h1>Hello, You are in ChaiAurCode home page</h1>")
    return render(request, 'website/index.html')

def about(request): # this method can be any name
    return HttpResponse("<h1>Hello, You are in ChaiAurCode about page</h1>")

def contact(request): # this method can be any name
    return HttpResponse("<h1>Hello, You are in ChaiAurCode contact page</h1>")