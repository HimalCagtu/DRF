from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

 
class UserForm(ModelForm):

    password = forms.PasswordInput()
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['name', 'email', 'username','password']
        

class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']