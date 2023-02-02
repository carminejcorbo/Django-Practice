from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .view_interface import checkcredentials, check_login, redirect_to_blog, redirect_to_login, does_user_exist, check_create_form

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if check_login(user):
            login(request, user)
            # Redirect to a success page.
            return redirect_to_blog(request)
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('There was an error logging in to your account. Incorrect username and/or password.'))
            return redirect_to_login(request)
        
    return render(request, 'login.html') # points toward our login.html file in the

def create_user(request):
    if request.method == 'POST':
        user_object = {
            'fname': request.POST['fname'],
            'lname': request.POST['lname'],
            'username': request.POST['username'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'retype': request.POST['retype']
        }
       
        if does_user_exist(user_object['username']):
            print("User name exists")
            return redirect_to_login(request)
        
        if does_user_exist(user_object['username']) == False:
            print("Insert some logic to create a new user. Then redirect to blog.")
            
            if False == False:
                print("Not enough information")
                messages.success(request, ('Please enter the correct information'))
                return redirect('create')      
            else:
                print("create new user , success")
                return redirect_to_blog(request)        
    return render(request,'create.html')
