from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
from newapp.models import Post



# Create your views here.
def blog(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts.html' , context)

def home(request):
    return render(request, 'base.html')