from django.urls import path, re_path

from . import views # import views so we can use them in urls.

urlpatterns = [
    #path('', views.index, name='index'),
    re_path(r'^$', views.listing, name='listing'),
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^search/$', views.search, name='search'),
]