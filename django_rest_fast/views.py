from django.shortcuts import render
from django.http import JsonResponse

from .conf import DJANGO_REST_FAST
from .format import method_description, method_url
from .schema import methods_list


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

    for fn, params in methods_list():
        url = method_url(params)
        
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

        method_name, method_desc = method_description(fn._doc)
        method = {
            fn._method: {
                'summary': method_name,
                'description': method_desc,
                'tags': fn._tags,
                'parameters': parameters,
            }
        }
        data['paths'][url] = method
    return JsonResponse(data)
