from inspect import isfunction
from typing import List, Dict

from django.urls import get_resolver
from django.forms import Form

from .conf import DJANGO_REST_FAST
from .format import method_description, method_url


def methods_list():
    """List of DRF decorated views methods."""
    items = []
    url_resolver = get_resolver()
    for fn, params in url_resolver.reverse_dict.items():
        if isfunction(fn) and fn.__name__ == 'drf_wrapper':
            items.append((fn, params))
    return items


def form_params(form: Form, http_method) -> List:
    """Get form parameters."""
    params = []
    for field in form():
        params.append({
            'in': 'query' if http_method == 'get' else 'body',
            'name': field.name,
            'required': field.field.required,
            'description': field.help_text,
            'schema': {
                'type': 'string'
            }
        })
    return params


def generate_method_schema(fn, params) -> Dict:
    parameters = form_params(fn.form, fn.http_method) if fn.form else []
    method_name, method_desc = method_description(fn.doc)
    method_schema = {
        fn.http_method: {
            'summary': method_name,
            'description': method_desc,
            'tags': fn.tags,
            'parameters': parameters,
            'responses': {},
        }
    }
    return method_schema


def generate_schema() -> Dict:
    """Generate swagger schema."""
    schema = {
        'openapi': '3.0.0',
        'info': DJANGO_REST_FAST['info'],
        'servers': [
            {
                'url': 'http://localhost:3090',  # fixme
            },
        ],
        'paths': {},
    }

    for fn, params in methods_list():
        url = method_url(params)
        method_schema = generate_method_schema(fn, params)
        schema['paths'][url] = method_schema
    return schema
