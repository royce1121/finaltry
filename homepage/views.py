from .models import Post
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User

def login(request):
    return render(request, 'homepage/login.html', {})

def logout_view(request):
    logout(request)
    return render(request, 'homepage/login.html', {})

def signup(request):
    return render(request, 'homepage/LoginPage.html', {})

def create(request):
	if request.POST:
		username = request.POST['user']
		password = request.POST['pass']
		email = request.POST['mail']
		user = User.objects.create_user(username, email, password)
		user.save()
		return render(request, 'homepage/login.html', {})

def check(request):
    if request.POST:
        username = request.POST['user']
        password = request.POST['pass']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'homepage/login.html', {})
        else:
            return render(request, 'homepage/login.html', {})
   