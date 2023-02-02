from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User

def does_user_exist(user):
    if User.objects.filter(username=user).exists():
        return True
    return False
    
def checkcredentials(username , password):
    if username!="" and password != "":
        return True
    else:
        return False 
def check_login(user):
    if user is not None:
        return True
    else:
        return False

def redirect_to_blog(request):
    return redirect('blog')

def redirect_to_login(request):
    return redirect('login')

def check_create_form():
    return False