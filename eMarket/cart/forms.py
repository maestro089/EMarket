from django import forms
from .models import *


class form_adress(forms.ModelForm):
    class Meta():
        model = user_adress
        fields = ('postal_code','country','sity','street','num_home')

        postal_code = forms.CharField(label="NPostal code", min_length=2, max_length=100,
                                widget=forms.TextInput(attrs={'class': 'class'}))
        country = forms.CharField(label='Country', 
                                  widget=forms.TextInput(attrs={'class': 'class'}))
        sity = forms.CharField(label='Sity', 
                                  widget=forms.TextInput(attrs={'class': 'class'}))
        street = forms.CharField(label='Street', 
                                 widget=forms.TextInput(attrs={'class': 'class'}))
        num_home = forms.CharField(label='Number home', 
                                  widget=forms.TextInput(attrs={'class': 'class'}))