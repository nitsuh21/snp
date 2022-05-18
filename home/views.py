from multiprocessing import context
from django.shortcuts import redirect, render
from ecommerce.models import Product,Shop

# Create your views here.
def home(request):
    return render(request,'welcome.html')