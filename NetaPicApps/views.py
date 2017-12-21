from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Image

def index(request):
    return render(request, "NetaPicApps/index.html")

def save_images(request):
    ImageTags = request.POST.get("tags","")
    files = request.FILES.getlist("files")
    ImageHolder = Image(tags = ImageTags)
    ImageHolder = Image(image = files[0])
    ImageHolder.save()
    return redirect("NetaPicApps:test")

def test_view(request):
    d = {
        'images': Image.objects.all(),
    }
    return render(request, "NetaPicApps/test.html", d)