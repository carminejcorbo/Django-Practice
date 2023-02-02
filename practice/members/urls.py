from . import views
from django.urls import include, path
from . import views


urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('create', views.create_user, name='create'),
]
