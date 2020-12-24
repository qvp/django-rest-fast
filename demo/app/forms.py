from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import get_user_model

from .models import Post

User = get_user_model()


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=20)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
