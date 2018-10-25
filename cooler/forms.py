from django import forms
from .models import Color
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ColorForm(forms.Form):
    title = forms.CharField(label='name', max_length=30, required=True, widget = forms.TextInput(
        attrs = {'class': 'my-input','placeholder': 'ColorTitle'}))
    colorCode = forms.CharField(label='colorCode' ,max_length=10, required=True, widget = forms.TextInput(
        attrs = {'class': 'my-input','placeholder': 'ColorCode'}))