from django.shortcuts import render
from django.http import JsonResponse

from .schema import generate_schema


def docs(request):
    return render(request, 'django_rest_fast/swagger-ui.html')


def schema(request):
    schema_dict = generate_schema()
    return JsonResponse(schema_dict)
