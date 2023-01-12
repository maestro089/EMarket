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


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Логин'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Имя'}))
    email = forms.CharField(label='Почта', widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Почта'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Пользователь с такой почтой уже есть!')
        return email
