from django.http import HttpRequest
from django.shortcuts import render,HttpResponse

# Create your views here.


def home(self):
    return HttpResponse("tema")