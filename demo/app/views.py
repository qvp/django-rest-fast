from django.http import QueryDict
from django.http.response import JsonResponse
from django_rest_fast.decorators import get, post, put, patch, delete
from django.contrib.auth.views import get_user_model

from .forms import (
    UserLoginForm,
    UserRegistrationForm,
    PostCreateForm,
)

User = get_user_model()


def demo_response(request):
    return JsonResponse({
        'message': 'This is a demo response',
        'you_send': {
            'query': request.GET,
            'body': QueryDict(request.body),
            'method': request.method,
        },
    })


@post(form=UserLoginForm, tags=['users'])
def users_login(request):
    """User login"""
    return demo_response(request)


@post(form=UserRegistrationForm, tags=['users'])
def users_registration(request):
    """User registration"""
    return demo_response(request)


@get(tags=['blog'])
def posts(request):
    """List of all blog posts"""
    return demo_response(request)


@post(form=PostCreateForm, tags=['blog'])
def posts_create(request):
    """
    Create new post.

    ### Markdown supported.
    * item one
    * item two
    """
    return demo_response(request)


@put(form=PostCreateForm, tags=['blog'])
def posts_update(request):
    """
    Update post.
    """
    return demo_response(request)


@patch(form=PostCreateForm, tags=['blog'])
def posts_update_partial(request):
    """
    Update post partial.
    """
    return demo_response(request)


@delete(tags=['blog'])
def posts_delete(request):
    """
    Delete post.
    """
    return demo_response(request)
