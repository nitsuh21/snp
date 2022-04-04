
from django.db import models

from accounts.models import User

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=50,unique=True,blank=True, null=True)
    phonenumber = models.CharField(max_length=50,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    street = models.CharField(max_length=50,blank=True, null=True)
    postalcode = models.CharField(max_length=50,blank=True, null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

class Product(models.Model):
    type = models.CharField(max_length=50,blank=True, null=True)
    name = models.CharField(max_length=150,blank=True, null=True)
    image = models.ImageField()
    price = models.CharField(max_length=50,blank=True, null=True)
    sale_price = models.CharField(max_length=50,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=50,blank=True, null=True)
    brand = models.CharField(max_length=50,blank=True, null=True)
    color = models.CharField(max_length=50,blank=True, null=True)
    size = models.CharField(max_length=50,blank=True, null=True)
    product_policy = models.TextField(blank=True, null=True)
    hasaffiliate = models.BooleanField(default=False)
    affiliatelink = models.CharField(max_length=150,blank=True, null=True) 
    affiliate = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,blank=True, null=True)




