from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from accounts.models import User
from django.core.mail import send_mail
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts import serializers

# Create your api views here.
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many = True)
    return Response(serializer.data)
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username has already taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email has already taken')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return render(request,'home.html')
        else:
            return render(request,'register.html')
        
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        user=auth.authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credential')
            print('invalid')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return render(request,'home.html')
        else:
            return render(request,'login.html')
        
def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('login')
    