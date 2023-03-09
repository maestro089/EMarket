from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


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
        'profile':profile_user
        }

    return render(request,"moderator/moderator_main.html",context = context)

def moderator_book(request):

    books = book.objects.all()

    context = {
        'books':books
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

class create_book(CreateView ):
    model = book
    template_name = 'moderator/edit_book_cart.html'

    form_class = EditBookForm


def delete_book(request,pk):

    b = book.objects.filter(pk = pk)
    path = request.path
    b.delete()

    return redirect('moderator:moderator_main')

def manager_main(request):
    if request.method == 'POST':
            id = request.GET.get("order_id")
            order =  Order.objects.get(pk = id)
            order.status = request.POST.get("status")
            order.save()


    orders =  Order.objects.all()
    books = BookInOrder.objects.all()
    context = {
        'orders':reversed(orders),
        'books':books
        }
    return render(request,'manager/index.html',context = context)


def comment(request):
    comments = comment_book.objects.all().order_by("-id")
    context ={
        'comments':comments,
        }
    return render(request,'moderator/comment_moderator.html',context = context)
    


