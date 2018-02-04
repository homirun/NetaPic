from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Image

def index(request):
    return render(request, "NetaPicApps/index.html")

def save_images(request):
    ImageTags = request.POST.get("tags")
    files = request.FILES.getlist("files")
    ImageHolder = Image(image = files[0], tags = ImageTags)
    ImageHolder.save()
    return redirect("NetaPicApps:test")

def test_view(request):
    SearchKeyword = request.GET.get("tags")
    ImageUrl = []
    if SearchKeyword == None or SearchKeyword == "" :
        for i in Image.objects.all():
            ImageUrl.append(i.image)
    else:
        for i in Image.objects.filter(tags = SearchKeyword):
            ImageUrl.append(i.image)
    d = {
        'images':ImageUrl ,
    }
    return render(request, "NetaPicApps/test.html", d)

def remove_images(id):
    Image.objects.filter(id = id).delete()