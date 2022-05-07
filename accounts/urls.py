from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .apiviews import RegisterAPI,LoginAPI
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('users/',views.getUsers,name='getUsers'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
]