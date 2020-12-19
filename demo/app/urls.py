from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts),
    path('posts/create', views.posts_create),
    path('users/login', views.users_login),
    path('users/registration', views.users_registration),
]
