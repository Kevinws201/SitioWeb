from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    carrera = forms.ChoiceField(choices=CustomUser.CARRERA_CHOICES)
    nivel_educativo = forms.ChoiceField(choices=CustomUser.NIVEL_EDUCATIVO_CHOICES)    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name','carrera', 'nivel_educativo', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Username"),
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    