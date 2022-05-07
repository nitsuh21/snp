from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50,blank=True, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    firstname = models.CharField(max_length=50,blank=True, null=True)
    middlename = models.CharField(max_length=50,blank=True, null=True)
    lastname = models.CharField(max_length=50,blank=True, null=True)
    phonenumber = models.CharField(max_length=50,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    street = models.CharField(max_length=50,blank=True, null=True)
    postalcode = models.CharField(max_length=50,blank=True, null=True)
    
    def __str__(self):
        return "{}".format(self.username)
