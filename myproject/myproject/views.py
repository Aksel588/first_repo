# from django.http import HttpResponse
from urllib import request

from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello, world")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("Me about page")
    return render(request, 'about.html')