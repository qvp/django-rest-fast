from django import forms

from .models import User


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    price = forms.CharField(min_length=8, max_length=20)


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
