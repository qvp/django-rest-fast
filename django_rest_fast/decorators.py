def get(form=None, tags=None):
    return _decorator('get', form, tags)


def post(form=None, tags=None):
    return _decorator('post', form, tags)


def _decorator(method, form, tags):
    def decorator(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        wrapper._doc = function.__doc__
        wrapper._form = form
        wrapper._tags = tags
        wrapper._method = method
        return wrapper
    return decorator
