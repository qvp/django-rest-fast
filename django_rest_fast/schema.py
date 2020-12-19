from inspect import isfunction
from typing import Dict, List

from django.urls import get_resolver

from .conf import DJANGO_REST_FAST
from .format import method_description, method_url
from .forms import form_schema


def methods_list() -> List:
    """List of DRF decorated views methods."""
    items = []
    url_resolver = get_resolver()
    for fn, params in url_resolver.reverse_dict.items():
        if isfunction(fn) and fn.__name__ == 'drf_wrapper':
            items.append((fn, params))
    return items


def method_schema(fn, params) -> Dict:
    parameters = form_schema(fn.form, fn.http_method) if fn.form else []
    method_name, method_desc = method_description(fn.doc)
    method_schema_ = {
        fn.http_method: {
            'summary': method_name,
            'description': method_desc,
            'tags': fn.tags,
            'parameters': parameters,
            'responses': {},
        }
    }
    return method_schema_


def api_schema(server_url) -> Dict:
    """Generate api schema."""
    schema = {
        'openapi': '3.0.0',
        'info': DJANGO_REST_FAST['info'],
        'servers': DJANGO_REST_FAST['servers'] if DJANGO_REST_FAST['servers'] else [{'url': server_url}],
        'paths': {},
    }

    for fn, params in methods_list():
        url = method_url(params)
        schema['paths'][url] = method_schema(fn, params)
    return schema
