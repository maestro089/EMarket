from django.shortcuts import render, redirect
from .models import * 
from django.contrib.auth.models import User

def index(request):
    ad = book.objects.all()
    genre = genre_of_the_book.objects.all()

    context ={
        'photo_user':profile.objects.filter(user = request.user),
        'ad':ad,
        'genre':genre,
        }
    return render(request,'main/index.html',context = context)

def ad_info(request, ad_id):
    ad = book.objects.filter(id = ad_id)
    search_book = book.objects.get(id = ad_id)
    comment = comment_book.objects.filter(book_in_comment = ad_id)

    if request.method == "POST":
        comment_book.objects.create(author = request.user,text = request.POST.get('Text'),book_in_comment=search_book)
        return redirect(request.path)

    context ={
        'ad':ad,
        'comment':comment,
        'photo_user':profile.objects.filter(user = request.user),
        }
    return render(request,'main/ad.html',context = context)

def home(request):

    books = book.objects.all().order_by("-id")[0:4]
    author = Author_of_the_book.objects.all().order_by("-id")[0:4]

    context = {
        "books":books,
        "author":author,
        'photo_user':profile.objects.filter(user = request.user),
        }

    return render(request,'main/home.html',context = context)

def profile_user(request):
    moder = profile.objects.filter(user = request.user)
    context ={
        'moder':moder,
        'photo_user':profile.objects.filter(user = request.user),
        }
    return render(request,"main/profile.html",context = context)




