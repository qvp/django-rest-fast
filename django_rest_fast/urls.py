from django.urls import path

from .views import docs, schema

urlpatterns = [
    path('', docs, name='drf-docs'),
    path('schema/', schema, name='drf-schema'),
]
