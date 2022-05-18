
from distutils.command.upload import upload
import email
from email import policy
from unicodedata import category
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail

from accounts.models import User

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=50,unique=True,blank=True, null=True)
    phonenumber = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    street = models.CharField(max_length=50,blank=True, null=True)
    postalcode = models.CharField(max_length=50,blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    shippingpolicy = models.TextField(blank=True, null=True)
    refundpolicy = models.TextField(blank=True, null=True)
    cre_policy = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="images/stores/",blank=True, null=True)
    banner = models.ImageField(upload_to="images/stores/",blank=True, null=True)
    rate = models.CharField(max_length=50,blank=True, null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

class Product(models.Model):
    category = models.CharField(max_length=50,blank=True, null=True)
    type1 = models.CharField(max_length=50,blank=True, null=True)
    type2 = models.CharField(max_length=50,blank=True, null=True)
    name = models.CharField(max_length=150,blank=True, null=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/products/")
    condition = models.CharField(max_length=50,blank=True, null=True)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=50,blank=True, null=True)
    brand = models.CharField(max_length=50,blank=True, null=True)
    model = models.CharField(max_length=50,blank=True, null=True)
    color = models.CharField(max_length=50,blank=True, null=True)
    size = models.CharField(max_length=50,blank=True, null=True)
    guarantee = models.CharField(max_length=100,blank=True, null=True)
    product_policy = models.TextField(blank=True, null=True)
    hasaffiliate = models.BooleanField(default=False)
    affiliatepercentage = models.CharField(max_length=50,blank=True, null=True)
    affiliatelink = models.CharField(max_length=150,blank=True, null=True) 
    affiliate = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,blank=True, null=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/products/")

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1,blank=True, null=True)
    Subtotal = models.IntegerField(default=0,blank=True, null=True)
    Total = models.IntegerField(default=0,blank=True, null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return self.product.name




