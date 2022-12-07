from django.shortcuts import render, redirect
from .models import * 
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from news.models import news


def index(request):
    ad = book.objects.all()
    genre = genre_of_the_book.objects.all()

    if request.user.is_authenticated:
        photo_user=profile.objects.filter(user = request.user)
    else:
        photo_user = ""

    context ={
        'photo_user':photo_user,
        'ad':ad,
        'genre':genre,
        }
    return render(request,'main/index.html',context = context)

def ad_info(request, ad_id):
    ad = book.objects.filter(id = ad_id)
    search_book = book.objects.get(id = ad_id)
    comment = comment_book.objects.filter(book_in_comment = ad_id)

    if request.user.is_authenticated:
        photo_user=profile.objects.filter(user = request.user)
    else:
        photo_user = ""

    if request.method == "POST":
        comment_book.objects.create(author = request.user,text = request.POST.get('Text'),book_in_comment=search_book)
        return redirect(request.path)

    context ={
        'ad':ad,
        'comment':comment,
        'photo_user':photo_user,
        }
    return render(request,'main/ad.html',context = context)

def home(request):
    if request.user.is_authenticated:
        photo_user=profile.objects.filter(user = request.user)
    else:
        photo_user = ""

    context = {
        "books":book.objects.all().order_by("-id")[0:4],
        "author":Author_of_the_book.objects.all().order_by("-id")[0:4],
        'photo_user':photo_user,
        'news':news.objects.all().order_by("-id")[0:4],
        }

    return render(request,'main/home.html',context = context)

def profile_user(request):
    moder = profile.objects.filter(user = request.user)
    if request.user.is_authenticated:
        photo_user=profile.objects.filter(user = request.user)
    else:
        photo_user = ""
    context ={
        'moder':moder,
        'photo_user':photo_user,
        }
    return render(request,"main/profile.html",context = context)

def contact(request):

    if request.user.is_authenticated:
        photo_user=profile.objects.filter(user = request.user)
    else:
        photo_user = ""

    context={
        'photo_user':photo_user,
        }
    return render(request,"main/contact.html",context = context)


class edit_profile(UpdateView):
    model = User
    template_name = 'main/porfile.html'

    fields = ['username', 'last_name', 'first_name', 'email']




