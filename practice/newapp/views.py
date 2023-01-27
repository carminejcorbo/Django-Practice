from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
from newapp.models import Post



# Create your views here.
def home(request):
    template = loader.get_template('posts.html')
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts.html' , context)