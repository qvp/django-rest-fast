from typing import List

from django.urls.converters import (
    IntConverter,
    StringConverter,
)


def path_schema(params) -> List:
    """Generate path params schema"""
    items = []
    try:
        for name, type_ in params[3].items():
            if isinstance(type_, IntConverter):
                type_str = 'integer'
            elif isinstance(type_, StringConverter):
                type_str = 'string'
            else:
                type_str = 'string'
            items.append({
                'in': 'path',
                'name': name,
                # 'required': True,  # fixme
                'schema': {
                    'type': type_str,
                }
            })
    except IndexError:
        pass
    return items
