from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Image

#index
def index(request):
    return render(request, "NetaPicApps/index.html")

#画像保存時
def save_images(request):

    #登録されたタグと画像
    ImageTags = request.POST.get("tags")
    files = request.FILES.getlist("files")

    #保存
    ImageHolder = Image(image = files[0], tags = ImageTags)
    ImageHolder.save()

    return redirect("NetaPicApps:test")

#画像出力
def test_view(request):

    #検索タグ
    SearchKeyword = request.GET.get("tags")

    #検索タグを用いてDBから画像データの抜き出し
    ImageUrl = []
    if SearchKeyword == None or SearchKeyword == "" :
        for i in Image.objects.all():
            ImageUrl.append(i)
    else:
        for i in Image.objects.filter(tags = SearchKeyword):
            ImageUrl.append(i)

    #テンプレートに渡すデータ
    d = {
        'images':ImageUrl ,
    }

    return render(request, "NetaPicApps/test.html", d)

#DBからの画像の削除
def remove_images(id):
    Image.objects.filter(id = id).delete()