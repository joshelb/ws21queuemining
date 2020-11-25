from django.shortcuts import render
from django.http import HttpResponse,request
# Create your views here.
from .processmining.test import xd

def index(request):
    output =
    return HttpResponse(output)
