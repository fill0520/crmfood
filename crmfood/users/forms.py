from django import forms
from django.contrib.auth import authenticate
from .models import User

class Registration(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password',)

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)