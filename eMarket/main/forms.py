from django.forms import ModelForm
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'type':'text',  'name':'txtSub', 'class':'form-control', 'placeholder':'Тема'}))
    email_address = forms.EmailField(max_length=150,widget=forms.TextInput(attrs={'type':'text',  'name':'txtУьфшд', 'class':'form-control', 'placeholder':'Почта'}))
    message = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Сообщение'}),
                              max_length=2000)

