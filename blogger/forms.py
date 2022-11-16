from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Blog


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Re-enter password', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

