from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.views.generic import UpdateView


from main.models import comment_book,profile,book,Author_of_the_book,genre_of_the_book
from .forms import EditBookForm, EditNewsForm
from news.models import news
from cart.models import Order,BookInOrder


def moderator_main(request):

    books = comment_book.objects.all()
    user = User.objects.all()
    profile_user = profile.objects.all()

    context = {
        'books':books,
        'user':user,
        'profile':profile_user,
        'photo_user':profile.objects.filter(user = request.user),
        }

    return render(request,"moderator/moderator_main.html",context = context)

def moderator_book(request):

    books = book.objects.all()

    context = {
        'books':books,
        'photo_user':profile.objects.filter(user = request.user),
        }

    return render(request,"moderator/moderator_book.html",context = context)

def delete_user(request):
    path = request.GET.get('next')

    user_search = User.objects.get(id = request.GET.get('user_id'))
    user_search.delete()


    return redirect(path)

def add_menejer(request,pk):
    profile_user = profile.objects.get(id = pk)
    profile_user.moderator = True
    profile_user.save()

    return redirect('moderator:moderator_main')

def delete_menejer(request,pk):

    profile_user = profile.objects.get(id = pk)
    profile_user.moderator = False
    profile_user.save()

    return redirect('moderator:moderator_main')

class edit_book(UpdateView):
    model = book
    template_name = 'moderator/edit_book_cart.html'

    form_class = EditBookForm

def moderator_news(request):

    search_news = news.objects.all()

    context ={
        "news":search_news,
        'photo_user':profile.objects.filter(user = request.user),
        }

    return render(request,"moderator/moderator_news.html",context = context)

class edit_news(UpdateView):
    model = news
    template_name = 'moderator/edit_news_cart.html'

    form_class = EditNewsForm

def manager_main(request):
    orders =  reversed(Order.objects.all())
    books = BookInOrder.objects.all()
    context = {
        'orders':orders,
        'books':books,
        'photo_user':profile.objects.filter(user = request.user),
        }
    return render(request,'manager/index.html',context = context)

    


