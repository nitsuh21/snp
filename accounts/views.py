from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from accounts.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication

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
            return redirect('signin')
    else:
        if request.user.is_authenticated:
            return render(request,'index.html')
        else:
            return render(request,'register.html')
        
def signin(request):
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
            return redirect('signin')
    else:
        if request.user.is_authenticated:
            return redirect('feed')
        else:
            return render(request,'login.html')

def signout(request):
    auth.logout(request)
    return redirect('signin')
       
def home(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return redirect('signin')


def serialize_user(user):
    return {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })
        

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })


@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_data': serialize_user(user)
        })
    return Response({})