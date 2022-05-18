from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .router import router

urlpatterns = [
    path('',views.marketplace,name='marketplace'),
    path('stores/',views.stores,name='stores'),
    path('mystores/',views.mystores,name='mystores'),
    path('storeprofile/<str:name>/',views.storeprofile,name='storeprofile'),
    path('store_edit/<str:name>/',views.store_edit,name='store_edit'),
    path('productdetail/<str:id>/',views.productdetail,name='productdetail'),
    path('products',views.products,name='products'),
    path('addproduct/<str:name>/',views.addproduct,name='addproduct'),
    path('addtocart/<str:id>/',views.addtocart,name='addtocart'),
    path('createshop',views.createshop,name='createshop'),
    path('updatecart',views.updatecart,name='updatecart'),
    path('categories/<str:name>/',views.categories,name='categories'),
    path('cart',views.cart,name='cart'),
    path('add',views.add,name='add'),
    path('api/',include(router.urls))
]