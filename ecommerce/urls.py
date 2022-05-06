from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .router import router

urlpatterns = [
    path('',views.marketplace,name='marketplace'),
    path('stores/',views.stores,name='stores'),
    path('storeprofile/<str:name>/',views.storeprofile,name='storeprofile'),
    path('productdetail/<str:name>/',views.productdetail,name='productdetail'),
    path('products',views.products,name='products'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('createshop',views.createshop,name='createshop'),
    path('add',views.add,name='add'),
    path('api/',include(router.urls))
]