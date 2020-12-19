from django.http.response import JsonResponse
from django_rest_fast.decorators import get, post

from .forms import UserLoginForm, UserRegistrationForm


@post(form=UserLoginForm, tags=['users'])
def users_login(request):
    """User login"""
    return JsonResponse({'request_data': request.POST})


@post(form=UserRegistrationForm, tags=['users'])
def users_registration(request):
    """User registration"""
    return JsonResponse({'request_data': request.POST})


@get(tags=['blog'])
def posts(request):
    """List of all blog posts"""
    return JsonResponse({'items': []})


@post(tags=['blog'])
def posts_create(request):
    """
    Create new post.

    ### Method description.
    * aaa
    * bbb
    """
    # form = BarForm(data=request.POST)
    # if request.method == 'POST' and form.is_valid():
    #     print('OK!')
    return JsonResponse({'request_data': request.POST})
