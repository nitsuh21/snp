from itertools import product
from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from ecommerce.models import Product,Shop,ProductImage,Cart
# Create your views here.
def marketplace(request):
    products = Product.objects.all()
    for product in products:
        print(product.id)
        print(product.image.url)
    shops = Shop.objects.all()
    affiliatedproducts = Product.objects.filter(hasaffiliate=True)
    cart = Cart.objects.filter(owner=request.user)
    print(cart)
    context = {
        'products':products,
        'shops':shops,
        'affiliatedproducts':affiliatedproducts,
        'cart':cart
    }
    return render(request,'marketplace/marketplace.html',context)
def createshop(request):
    name = request.POST.get('name')
    country = request.POST.get('country')
    city = request.POST.get('city')
    phonenumber = request.POST.get('phonenumber')
    shop = Shop(name = name,country = country,city = city,phonenumber = phonenumber)
    shop.save()
    return redirect('/marketplace/mystores')

def addproduct(request):
    pass

def mystores(request):
    shops = Shop.objects.all().order_by("-id")
    context = {
        'shops':shops,
    }
    return render(request,'marketplace/myshops.html',context)

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
def addproduct(request,name):
    print(request.method)
    if request.method == 'GET':
        shop = Shop.objects.get(name=name)
        context ={
            'shop':shop
        }
        return render(request,'marketplace/addproduct.html',context)
    else:
        shop = Shop.objects.get(name=name)
        name = request.POST.get('name')
        hasaffiliate = request.POST.get('isaffiliate')
        price = request.POST.get('price')
        sale_price = request.POST.get('sale_price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        images = request.FILES.getlist('images')
        sku = request.POST.get('sku')
        brand = request.POST.get('brand')
        color = request.POST.get('color')
        size = request.POST.get('size')
        product_policy = request.POST.get('product_policy')
        print(shop)
        print(images)
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
        for image in images:
            productimage = ProductImage(product=product,image=image)
            productimage.save()
        return redirect('/marketplace/mystores')

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
    return redirect('storeprofile')

def stores(request):
    shops = Shop.objects.all()
    context = {
        'shops':shops
    }
    return render(request,'marketplace/stores.html',context)

def categories(request,name):
    products = Product.objects.filter(type1=name)
    context={
        'products':products
    }
    return render(request,'marketplace/bycategory.html',context)
def storeprofile(request,name):
    shop = Shop.objects.get(name=name)
    products = Product.objects.filter(shop=shop).order_by('-id')
    context ={
        'shop':shop,
        'products':products
    }
    return render(request,'marketplace/storeprofile.html',context)

def productdetail(request,id):
    product = Product.objects.get(id=id)
    altimages = ProductImage.objects.filter(product=product)
    moreproductsfromthisvendor = Product.objects.filter(shop=product.shop).exclude(id=id)
    relatedproducts = Product.objects.filter(type1=product.type1)
    moreproducts = Product.objects.filter(category=product.category)[:5]
    print(product.shop)
    print(moreproducts)
    print(relatedproducts)
    context ={
        'product':product,
        'moreproductsfromthisvendor':moreproductsfromthisvendor,
        'relatedproducts':relatedproducts,
        'moreproducts':moreproducts,
        'altimages':altimages
    }
    return render(request,'marketplace/productdetail.html',context)

def store_edit(request,name):
    shop = Shop.objects.get(name=name)
    context ={
        'shop':shop
    }
    return render(request,'marketplace/editshop.html',context)

def cart(request):
    cart = Cart.objects.filter(owner=request.user)
    for product in cart:
        product.product.subtotal = product.product.sale_price
    print(cart)
    print(product)
    context = {
        'cart':cart
    }
    return render(request,'marketplace/cart.html',context)

def addtocart(request,id):
    product = Product.objects.get(id=id)
    cart = Cart(product=product,owner=request.user)
    cart.save()
    return redirect('marketplace')

def updatecart(request):
    return redirect('cart')