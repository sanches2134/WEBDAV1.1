from django.urls import path,include,re_path

from .import views

urlpatterns=[
   # re_path(r'upload$',views.upload),
    #re_path(r'upload/$',views.upload),
    re_path(r'create$',views.create),
    re_path(r'create/$',views.create),
    re_path(r'download$',views.download),
    re_path(r'download/$',views.download),
    re_path(r'delete$',views.delete),
    re_path(r'delete/$',views.delete),
    re_path(r'^',views.index),
   
    ]
