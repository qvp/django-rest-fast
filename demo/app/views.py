from django.http.response import JsonResponse
from django_rest_fast.decorators import get, post

from .forms import BarForm


@get(tags=['demo'])
def foo(request):
    return JsonResponse({'result': 'foo'})


@post(form=BarForm, tags=['demo'])
def bar(request):
    """Bar method."""
    form = BarForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        print('OK!')
    return JsonResponse({'result': 'bar'})


@post(form=BarForm, tags=['users'])
def users_create(request):
    """
    Create user.

    ### Method description.
    * aaa
    * bbb
    """
    form = BarForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        print('OK!')
    return JsonResponse({'result': 'users_create'})
