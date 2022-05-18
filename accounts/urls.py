from django.urls import path
from . import views,apiviews
from django.contrib.auth import views as auth_views
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('api/user/', apiviews.get_user),
    path('api/login/', apiviews.login),
    path('api/register/', apiviews.register),
    path('api/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('users/',views.getUsers,name='getUsers'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('',views.home,name='home')
]