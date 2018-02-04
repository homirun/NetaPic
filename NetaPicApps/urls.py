from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'NetaPicApps'
urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^images/$', views.save_images, name = "images_dir"),
    url(r'^test/$',views.test_view, name = "test"),
    #url(r'^document/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)