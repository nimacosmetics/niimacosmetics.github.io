from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'register.html',{'error':'Sorry Username Taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('index')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        user = auth.authenticate(username = request.POST['username'], 
        password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return render(request,'login.html',{'error':'Username or Password is incorrect'})
    else:
        return render(request,'login.html')
    return render(request,"login.html")

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

def index(request):
    return render(request, 'index.html')
def products(request):
    return render(request, 'products.html')
def single(request):
    return render(request, 'single-product.html')
