def get(form=None, tags=None):
    return _decorator('get', form, tags)


def post(form=None, tags=None):
    return _decorator('post', form, tags)


def _decorator(method, form, tags):
    def decorator(function):
        def drf_wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        drf_wrapper._doc = function.__doc__
        drf_wrapper._form = form
        drf_wrapper._tags = tags
        drf_wrapper._method = method
        return drf_wrapper
    return decorator
