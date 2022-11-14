from django.shortcuts import render, redirect
from .models import * 

def index(request):
    ad = book.objects.all()
    context ={
        'ad':ad,
        }
    return render(request,'main/index.html',context = context)

def ad_info(request, ad_id):
    ad = book.objects.filter(id = ad_id)
    context ={
        'ad':ad,
        }
    return render(request,'main/ad.html',context = context)

def home(request):
    return render(request,'main/home.html')

def profile_user(request):
    moder = profile.objects.filter(user = request.user)
    context ={
        'moder':moder,
        }
    return render(request,"main/profile.html",context = context)


