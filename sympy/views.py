from django.shortcuts import render


import requests

# Create your views here.


def hello(request):
    return render(request,'home.html',{})