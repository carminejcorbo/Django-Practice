from . import views
from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
]
