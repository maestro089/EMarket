from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage

from .models import the_cart,Order,BookInOrder,points_of_issue_adress
from main.models import book, genre_of_the_book,Author_of_the_book,profile
from .forms import *



def view_cart(request):

    price = 0
    
    cart_book = the_cart.objects.filter(customer = request.user)
    

    for cart_book in cart_book:
        price_book = book.objects.get(title = cart_book.title_book)
        price = price + price_book.price * cart_book.quentity


    cart_book = the_cart.objects.filter(customer = request.user)

    context = {
        'cart_book':cart_book,
        'price':price,
        }
    return render(request,'cart/cart_view.html',context = context)

def add_cart(request):
    path = request.GET.get('next')
    
    if request.method == 'POST':
        if request.POST.get('quentity_book'):
                the_cart.objects.create(title_book = book.objects.get(id = request.GET.get('ad_id')),
                                        customer = request.user, 
                                        quentity = request.POST.get('quentity_book')
                                        )
    return redirect(path)

def delete_cart(request):
    path = request.GET.get('next')
    
    if request.method == 'POST':
        book_id = request.GET.get('cart_id')
        find_book = the_cart.objects.get(id = book_id)
        find_book.delete()
    return redirect(path)

def place_order(request):
    list =''
    cart = the_cart.objects.filter(customer = request.user)
    if(len(cart)>0):
        order = Order.objects.create(customer=request.user, adress = points_of_issue_adress.objects.get(pk = request.POST.get('adress')))

        for cart in cart:
            product = book.objects.get(pk=cart.title_book.pk)
            quantity = cart.quentity
            BookInOrder.objects.create(order=order, book=cart.title_book, quantity=quantity)
            cart.delete()
        for b in BookInOrder.objects.filter(order = order):
            list = list + str(b.book.title) + " Количество " + str(b.quantity) + "\n"
        email_body = "Заказчик: "+ str(request.user) + "\n" + list + "\n" + str(order.adress)
            
        email = EmailMessage('Заказ от' + str(order.created), email_body,to=['egor-karpov09@bk.ru'])
        email.send()
        messages.success(request, 'Заказ оформлен')
        return render(request,'cart/cart_view.html') 
    return render(request,'cart/cart_view.html')

def search(request):
    query_search = request.GET.get('search', '')
    
    ad = book.objects.filter(title__icontains = query_search)
    try:
        genre = genre_of_the_book.objects.get(title__icontains = query_search)
        ad_genre = book.objects.filter(genre = genre)
    except:
        ad_genre = ''

    context ={
        'ad':ad,
        'ad_genre':ad_genre,
        'query_search':query_search
        }
    return render(request,'main/seach_result.html',context = context)

def order(request):
    orders =  Order.objects.filter(customer = request.user)
    books = BookInOrder.objects.all()

    if request.user.is_authenticated:
        photo_user=profile.objects.filter(user = request.user)
    else:
        photo_user = ""
    context = {
        'orders':orders,
        'books':books,
        'photo_user':photo_user,
        }
    return render(request,'Order.html',context = context)

def filter_book(request):
    genre = genre_of_the_book.objects.all()


    if request.method == "GET":
        path = request.path
        ad = book.objects.all()
        if request.GET.get("author_name"):
            a = Author_of_the_book.objects.get(name__icontains = request.GET.get("author_name"))
            ad = ad.filter(Author = a.id)
        if request.GET.get("price_min"):
            ad = ad.filter(price__gte = request.GET.get("price_min"))
        if request.GET.get("price_max"):
            ad = ad.filter(price__lte = request.GET.get("price_max"))

    context ={
        'ad':ad,
        }

    return redirect(request.GET.get('next'))

def making_order(request):
    adress = points_of_issue_adress.objects.all()
    cart = the_cart.objects.filter(customer = request.user)

    context = {
        'adress':adress,
        'cart_book':cart
        }
    return render(request,'cart/making_order.html',context = context)
