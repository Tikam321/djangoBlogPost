from django import forms
# from django.contrib.auth.forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class registration_form(UserCreationForm):
    email=forms.EmailField(label='Email')

    class Meta:
        model=User
        fields=['username','email','password1','password2']


class update_register_form(forms.ModelForm):
    email=forms.EmailField(label='Email')

    class Meta:
        model=User
        fields=['username','email']

class update_profile_form(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['image']
