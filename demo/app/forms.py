from django import forms


class BarForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    price = forms.DecimalField(min_value=0.1)
    description = forms.CharField(max_length=1000, required=False)
