from django.shortcuts import render
from django.http import JsonResponse

from .schema import generate_schema


def docs(request):
    return render(request, 'django_rest_fast/swagger-ui.html')


def schema(request):
    server_url = 'http://localhost:' + request.META['SERVER_PORT']
    schema_dict = generate_schema(server_url)
    return JsonResponse(schema_dict)
