from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.hashers import make_password

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username,password=password).exists():
            user = User.objects.get(username=username)            
            request.session['user'] = str(user)
            request.session['create'] = True
            return redirect('post')
        else:
            messages.info(request, 'Please enter the right credentials')
            return redirect('login')

    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = make_password((request.POST['password']))
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is already taken')
            return redirect('signup')
        else:
            user = User.objects.create(username=username, password=password)
            user.save()
            request.session['user'] = str(user)
            request.session['create'] = True
            return redirect('post')
    return render(request, 'account/signup.html')

def logout(request):
    request.session['user'] = ""
    request.session['create'] = ""
    return redirect('login')