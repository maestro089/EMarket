from dataclasses import fields
from optparse import Option
from random import choice, choices
from sys import maxsize
from django.contrib.auth.forms import AuthenticationForm, UsernameField,UserCreationForm
from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'login'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'login'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

