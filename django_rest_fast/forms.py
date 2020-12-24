from typing import List, Dict

from django.forms import (
    Form,
    Field,
    IntegerField,
    BooleanField,
    FloatField,
    DecimalField,
    FileField,
)


def field_schema(field: Field) -> Dict:
    """Get data type of field."""
    if isinstance(field, BooleanField):
        return {
            'type': 'boolean',
        }
    if isinstance(field, FloatField) or isinstance(field, DecimalField):
        return {
            'type': 'number',
            'minimum': field.min_value,
            'maximum': field.max_value,
        }
    if isinstance(field, IntegerField):
        return {
            'type': 'integer',
            'minimum': field.min_value,
            'maximum': field.max_value,
        }
    if isinstance(field, FileField):
        return {
            'type': 'string',
            'format': 'binary',
        }
    # todo array, object
    return {
            'type': 'string',
        }


def form_schema(form: Form, http_method: str) -> List:
    """Get form parameters."""
    params = []
    for field in form():
        params.append({
            'in': 'query' if http_method == 'get' else 'body',
            'name': field.name,
            'required': field.field.required,
            'description': field.help_text,
            'schema': field_schema(field.field)
        })
    return params
