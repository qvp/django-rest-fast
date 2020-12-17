from inspect import isfunction

from django.shortcuts import render
from django.http import JsonResponse
from django.urls import get_resolver

from .conf import DJANGO_REST_FAST


def docs(request):
    return render(request, 'django_rest_fast/swagger-ui.html')


def schema(request):
    data = {
        'openapi': '3.0.0',
        'info': DJANGO_REST_FAST['info'],
        'servers': [
            {
                'url': 'http://localhost:3090',
            },
        ],
        'paths': {},
    }

    url_resolver = get_resolver()
    for fn, params in url_resolver.reverse_dict.items():
        if not isfunction(fn) or fn.__name__ != 'wrapper':
            continue

        url = '/' + params[0][0][0]
        url = url.replace('%(', '{')
        url = url.replace(')s', '}')

        parameters = None
        if fn._form:
            parameters = []
            for field in fn._form():
                parameters.append({
                    'in': 'query' if fn._method == 'get' else 'body',
                    'name': field.name,
                    # 'required': field.required,
                    'description': field.help_text,
                    'schema': {
                        'type': 'string'
                    }
                })

        method = {
            fn._method: {
                'summary': fn._doc,
                'tags': fn._tags,
                'parameters': parameters,
            }
        }
        data['paths'][url] = method
    return JsonResponse(data)
