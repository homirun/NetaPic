from django.conf.urls import url
from . import views

app_name = 'NetaPicApps'
urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^images/$', views.save_images, name = "images_dir"),
    url(r'^test/$',views.test_view, name = "test"),
]