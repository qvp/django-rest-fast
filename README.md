# Django REST Fast
Fast create REST API with Swagger documentation based on native django views and forms.
Automatically generates swagger documentation based on django forms and url config.

### Installation
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

### Example
```python
from django_rest_fast.decorators import get, post
from django.http.response import HttpResponse

from app.forms import BarForm


@get(tags=['demo'])
def foo(request):
    """ Foo method."""
    return HttpResponse('Foo')


@post(form=BarForm, tags=['demo'])
def bar(request):
    """ Bar method."""
    form = BarForm(data=request.POST)
    if form.is_valid():
        print('OK!')
    return HttpResponse('Bar')
```

### Configuration
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