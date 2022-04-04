from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .apiviews import RegisterAPI
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('users/',views.getUsers,name='getUsers'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
]