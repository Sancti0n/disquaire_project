from django.urls import path, re_path

from . import views # import views so we can use them in urls.

urlpatterns = [
    #path('', views.index), # "/store" will call the method "index" in "views.py"
    #path('', views.listing),
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail),
    path('search/', views.search),
]