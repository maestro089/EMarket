import re
from django.shortcuts import redirect,render
from django.contrib.auth.models import User


from main.models import comment_book,profile,book


def moderator_main(request):

    books = comment_book.objects.all()
    user = User.objects.all()
    profile_user = profile.objects.all()

    context = {
        'books':books,
        'user':user,
        'profile':profile_user
        }

    return render(request,"moderator/moderator_main.html",context = context)

def moderator_book(request):

    books = book.objects.all()

    context = {
        'books':books,
        }

    return render(request,"moderator/moderator_book.html",context = context)

def delete_user(request):
    path = request.GET.get('next')

    user_search = User.objects.get(id = request.GET.get('user_id'))
    user_search.delete()


    return redirect(path)

def add_menejer(request):
    path = request.GET.get('next')

    profile_user = profile.objects.get(user = request.GET.get('profile_id'))
    profile_user.moderator = True
    profile_user.save()

    return redirect(path)

def delete_menejer(request):
    path = request.GET.get('next')

    profile_user = profile.objects.get(user = request.GET.get('profile_id'))
    profile_user.moderator = False
    profile_user.save()

    return redirect(path)
