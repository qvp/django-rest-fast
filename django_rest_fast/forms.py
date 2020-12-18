from typing import List

from django.forms import (
    Form,
    Field,
    IntegerField,
    BooleanField,
    FloatField,
    DecimalField,
)


def field_type(field: Field) -> str:
    """Get data type of field."""
    if isinstance(field, IntegerField):
        return 'integer'
    if isinstance(field, BooleanField):
        return 'boolean'
    if isinstance(field, FloatField) or isinstance(field, DecimalField):
        return 'number'
    return 'string'


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
                'type': field_type(field),
            }
        })
    return params
