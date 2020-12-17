from inspect import isfunction

from django.urls import get_resolver


def methods_list():
    """List of DRF decorated views methods."""
    items = []
    url_resolver = get_resolver()
    for fn, params in url_resolver.reverse_dict.items():
        if isfunction(fn) and fn.__name__ == 'drf_wrapper':
            items.append((fn, params))
    return items
