from django.shortcuts import render
from django.http import JsonResponse

from .conf import DJANGO_REST_FAST
from .schema import methods_list, form_params, generate_schema


def docs(request):
    return render(request, 'django_rest_fast/swagger-ui.html')


def schema(request):
    schema_dict = generate_schema()
    return JsonResponse(schema_dict)
