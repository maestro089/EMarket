from main.models import book
from django.forms import ModelForm
from django import forms
from main.models import Author_of_the_book
from news.models import news


class EditBookForm(forms.Form,ModelForm):

    title = forms.CharField(label="Название", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Название'}))
    isbn = forms.CharField(label="isbn", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'isbn'}))
    #photo = forms.FileField(label="Фото", widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Фото'}))
    price = forms.IntegerField(label="Цена", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Цена'}))
    description = forms.CharField(label="Описание", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Описание'}))


    class Meta:
        model = book
        fields = ['photo','title', 'isbn', 'description', 'price','genre','Author']

class EditNewsForm(forms.Form,ModelForm):

    title = forms.CharField(label="Название", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Название'}))
    text = forms.CharField(label="Описание", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Описание'}))


    class Meta:
        model = news
        fields = ['photo','title', 'text']



        
