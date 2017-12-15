from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Image

def index(request):
    return render(request, "NetaPicApps/index.html")