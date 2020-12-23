from django.urls import path

from . import views

urlpatterns = [
    path('users/login', views.users_login),
    path('users/registration', views.users_registration),

    path('posts', views.posts),
    path('posts/create', views.posts_create),
    path('posts/update', views.posts_update),
    path('posts/update_partial', views.posts_update_partial),
]
