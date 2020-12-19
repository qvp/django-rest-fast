from django.urls import path

from app import views

urlpatterns = [
    path('', views.foo),
    path('bar/<int:id>/<str:hash>', views.bar),
    path('users/create', views.users_create),
]
