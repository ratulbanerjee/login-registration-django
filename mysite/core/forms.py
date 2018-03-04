from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user_name'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm_password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        def __init__(self,*args, **kwargs):
            super(UserCreationForm,self)._init_(*args,**kwargs)

