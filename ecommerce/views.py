from distutils.log import error
import imp
from itertools import product
from multiprocessing import context
from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import redirect, render
from ecommerce.models import Product,Shop,ProductImage,Cart,Order,OrderItem
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
import json
# Create your views here.
def marketplace(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        pcounter = products.count()
        p = Paginator(products,5)
        page = request.GET.get('page')
        products = p.get_page(page)
        shops = Shop.objects.all()
        affiliatedproducts = Product.objects.filter(hasaffiliate=True)
        cart = Cart.objects.filter(owner=request.user)
        order,created = Order.objects.get_or_create(customer=request.user,complete=False)
        items = order.orderitem_set.all().order_by('-id')
        cartItems = order.get_cart_items
        print(cartItems)
        context = {
            'products':products,
            'pcounter':pcounter,
            'shops':shops,
            'affiliatedproducts':affiliatedproducts,
            'cart':cart,
            'cartItems':cartItems,
            'items':'items'
        }
        return render(request,'marketplace/marketplace.html',context)
    else:
        products = Product.objects.all()
        pcounter = products.count()
        p = Paginator(products,5)
        page = request.GET.get('page')
        products = p.get_page(page)
        shops = Shop.objects.all()
        affiliatedproducts = Product.objects.filter(hasaffiliate=True)
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
        context = {
            'products':products,
            'pcounter':pcounter,
            'shops':shops,
            'affiliatedproducts':affiliatedproducts,
            'cartItems':cartItems,
            'items':'items'
        }
        return render(request,'marketplace/marketplace.html',context)

def createshop(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        city = request.POST.get('city')
        phonenumber = request.POST.get('phonenumber')
        try: 
            shop = Shop(name = name,country = country,city = city,phonenumber = phonenumber,owner=request.user)
            shop.save()
            return redirect('/marketplace/mystores') 
        except:
            messages.error(request,'Store name already exists')
            return redirect('/marketplace/mystores')
    else:
        return redirect('/marketplace/mystores')

def mystores(request):
    shops = Shop.objects.filter(owner=request.user).order_by("-id")
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

def maincategories(request,name):
    products = Product.objects.filter(category=name)
    print(products)
    names = request.POST.get('name')
    min = request.POST.get('min')
    max = request.POST.get('max')
    sizes = request.POST.get('size')
    brands = request.POST.getlist('brand')
    print(brands)
    colors = request.POST.get('color')
    for brand in brands:
        print(products.filter(brand=brand))
    print(products)
    category = name
    type1=[]
    size=[]
    brand=[]
    color=[]
    for product in products:
        if product.type1:
            type1.append(product.type1)
        if product.size:
            size.append(product.size)
        if product.brand:
            brand.append(product.brand)
        if product.color:
            color.append(product.color)
    context={
        'products':products,
        'type1':type1,
        'size':size,
        'brand':brand,
        'color':color,
        'category':category
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
    order,created = Order.objects.get_or_create(customer=request.user,complete=False)
    items = order.orderitem_set.all().order_by('-id')
    cartItems = order.get_cart_items
    print(cartItems)
    context = {
        'cartItems':cartItems,
        'items':items
    }
    return render(request,'marketplace/cart.html',context)

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = request.POST.get('product_id')
            product = Product.objects.get(id=prod_id)
            print(product)
            try:
                product_check = Product.objects.filter(id=prod_id)
                print(product_check)
                if product_check:
                    if Cart.objects.filter(owner=request.user,product=prod_id):
                        return JsonResponse({"status":"Product is already added to your cart"})
                    else:
                        prod_qty = request.POST.get('quantity')
                        cart = Cart(owner=request.user,product=product,Quantity=prod_qty)
                        cart.save()
                        return JsonResponse({"status":"Product added to your cart"})
                else:
                    return JsonResponse({"status":"No such product is found"})
            except Exception as er:
                print(er)
                return JsonResponse({"status":"No such product found"})
        else:
            return redirect('login')
    else:
        return redirect('/marketplace')


def updatecart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = request.POST.get('product_id')
            product = Product.objects.get(id=prod_id)
            print(product)
            try:
                product_check = Product.objects.filter(id=prod_id)
                print(product_check)
                if product_check:
                    if Cart.objects.filter(owner=request.user,product=prod_id):
                        prod_qty = request.POST.get('quantity')
                        cart = Cart.objects.get(owner=request.user,product=product)
                        cart.Quantity = prod_qty
                        cart.save()
                        return JsonResponse({"status":"Quantity Updated Successfully"})
                else:
                    return JsonResponse({"status":"No such product is found"})
            except Exception as er:
                print(er)
                return JsonResponse({"status":"No such product found"})
        else:
            return redirect('login')
    else:
        return redirect('cart')

def updateItem(request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        print('Action:', action)
        print('Product:', productId)

        customer = request.user
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(product.get_total)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product,seller=product.shop)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()
        print(orderItem)

        if orderItem.quantity <= 0:
            orderItem.delete()
        return JsonResponse('Item was added', safe=False)
