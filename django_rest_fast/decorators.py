def get(form=None, tags=None):
    """Add method to swagger doc as GET."""
    return _decorator('get', form, tags)


def post(form=None, tags=None):
    """Add method to swagger doc as POST."""
    return _decorator('post', form, tags)


def _decorator(http_method, form, tags):
    def decorator(function):
        def drf_wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        drf_wrapper.doc = function.__doc__
        drf_wrapper.form = form
        drf_wrapper.tags = tags
        drf_wrapper.http_method = http_method
        return drf_wrapper
    return decorator
