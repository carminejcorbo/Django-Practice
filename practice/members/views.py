from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('blog')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('There was an error logging in to your account.'))
            return redirect('login')
    return render(request, 'login.html') # points toward our login.html file in the


