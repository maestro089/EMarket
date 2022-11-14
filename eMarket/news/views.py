from django.shortcuts import render, redirect
from .models import * 

def index(request):
    ad = news.objects.all()
    context ={
        'ad':ad,
        }
    return render(request,'new/index.html',context = context)
