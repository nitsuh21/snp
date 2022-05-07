from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .router import router

urlpatterns = [
    path('',views.feed,name='feed'),
    path('addpost',views.addpost,name='addpost'),
    path('api/',include(router.urls))
]