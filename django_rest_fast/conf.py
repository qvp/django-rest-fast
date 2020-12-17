from django.conf import settings

from .utils import dict_merge

DJANGO_REST_FAST = {
    'info': {
        'version': '0.0.1',
        'title': 'Django REST Fast',
        'description': '',
    },
}

try:
    dict_merge(DJANGO_REST_FAST, settings.DJANGO_REST_FAST)
except AttributeError:
    pass
