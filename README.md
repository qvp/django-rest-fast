# Django REST Fast
Fast create REST API with Swagger documentation based on native django views and forms.

## Features:
* Maximum native integration with django, it is enough to decorate the view.
* `Form` and `ModelForm` automatically parsed and added parameters into the swagger.
* Parameters in `urlpatterns` automatically parsed as path parameters and added to swagger.

## Documentation

* [Installation](#installation)
* [Getting Started](#getting-started)
* [Configuration](#configuration)
* [Demo](#demo)

## Installation
```shell
pip install django-rest-fast
```

```python
INSTALLED_APPS = [
    ...
    'django_rest_fast',
]
```

Add the following to your root `urls.py` file.
```python
urlpatterns = [
    ...
    path('docs/', include('django_rest_fast.urls'))
]
```

## Getting Started
```python
# forms.py
from django import forms

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=20)


# views.py
from django_rest_fast.decorators import post

@post(form=UserLoginForm, tags=['users'])
def users_login_view(request):
    """User login"""
    pass
```
More examples you can see in the [demo](#demo) application.

## Configuration
The default is the following configuration from `django_rest_fast.conf`:
```python
DJANGO_REST_FAST = {
    'info': {
        'version': '0.0.1',
        'title': 'Django REST Fast',
        'description': '',
    },
}
```
It's possible to override it in the `settings.py`. Configs will be merged.
```python
DJANGO_REST_FAST = {
    'info': {
        'version': '1.0.1',
    },
}
```

## Demo
Run demo:
* `git clone git@github.com:qvp/django-rest-fast.git`
* `cd django-rest-fast`
* `docker-compose up`
* go to [http://localhost:3090/docs/](http://localhost:3090/docs/)

![alt text](https://github.com/qvp/django-rest-fast/blob/main/demo/preview.png?raw=true)