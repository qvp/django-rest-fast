from django.urls import include, path

urlpatterns = [
    path('', include('app.urls')),
    path('docs/', include('django_rest_fast.urls')),
]
