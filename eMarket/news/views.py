from django.shortcuts import render, redirect
from .models import * 
from main.models import profile

def index(request):
    ad = news.objects.all()
    context ={
        'ad':ad,
        'photo_user':profile.objects.filter(user = request.user),
        }
    return render(request,'new/index.html',context = context)

def news_info(request,pk):
    news_search = news.objects.filter(pk = pk)
    comments = comment.objects.filter(news = news.objects.get(pk = pk))

    if request.method == "POST":
        comment.objects.create(author = request.user,text = request.POST.get('Text'),news=news.objects.get(pk = pk))
        return redirect(request.path)

    context={
        "ad":news_search,
        "comment":comments,
        'photo_user':profile.objects.filter(user = request.user),
        }

    return render(request,"new/news.html",context = context)
