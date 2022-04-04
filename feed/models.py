from cgitb import text
from django.db import models
from accounts.models import User
# Create your models here.

# Create your models here.
class Post(models.Model):
    text = models.TextField(blank=True,null=True)
    attachment = models.FileField(max_length=50,blank=True, null=True)
    sharedlink = models.CharField(max_length=500,blank=True, null=True)