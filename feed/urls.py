from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.feed,name='feed'),
    path('addpost',views.addpost,name='addpost'),
]