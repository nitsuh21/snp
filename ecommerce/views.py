from itertools import product
from multiprocessing import context
from django.shortcuts import redirect, render
from ecommerce.models import Product,Shop
# Create your views here.
def marketplace(request):
    products = Product.objects.all()
    shops = Shop.objects.all()
    affiliatedproducts = Product.objects.filter(hasaffiliate=True)
    context = {
        'products':products,
        'shops':shops,
        'affiliatedproducts':affiliatedproducts
    }
    return render(request,'marketplace/marketplace.html',context)
def createshop(request):
    name = request.POST.get('shopname')
    shop = Shop(name = name)
    shop.save()
    return redirect('products')
def products(request):
    products = Product.objects.all()
    shops = Shop.objects.all()
    affiliatedproducts = Product.objects.filter(hasaffiliate=True)
    context = {
        'products':products,
        'shops':shops,
        'affiliatedproducts':affiliatedproducts
    }
    return render(request,'products.html',context)
def addproduct(request):
    shops = Shop.objects.all()
    context = {
        'shops':shops
    }
    return render(request,'addproduct.html',context)
def add(request):
    name = request.POST.get('name')
    hasaffiliate = request.POST.get('isaffiliate')
    shopid = request.POST.get('shop')
    price = request.POST.get('price')
    sale_price = request.POST.get('sale_price')
    description = request.POST.get('description')
    image = request.POST.get('image')
    sku = request.POST.get('sku')
    brand = request.POST.get('brand')
    color = request.POST.get('color')
    size = request.POST.get('size')
    product_policy = request.POST.get('product_policy')
    print(shopid)
    shop = Shop.objects.get(id=shopid)
    print(shop)
    if hasaffiliate == 'on':
        hasaffiliate = True
        link = 'https://www.facebook.com/' + str(request.user.id) + '/' + str(name)
    else:
        hasaffiliate = False
        link = ''
    print('hasaffiliate')
    print(link)
    product = Product(name = name,hasaffiliate = hasaffiliate,affiliatelink = link,shop=shop,
    price = price,sale_price = sale_price,description = description,image=image,
    sku = sku,brand = brand,color = color,size=size,product_policy=product_policy)
    product.save()
    return redirect('products')

def stores(request):
    shops = Shop.objects.all()
    context = {
        'shops':shops
    }
    return render(request,'marketplace/stores.html',context)

def storeprofile(request,name):
    shop = Shop.objects.get(name=name)
    context ={
        'shop':shop
    }
    return render(request,'marketplace/storeprofile.html',context)

def productdetail(request,name):
    product = Product.objects.get(name=name)
    context ={
        'product':product
    }
    return render(request,'marketplace/productdetail.html',context)