from django.shortcuts import render, redirect
from django.contrib import messages

from .models import the_cart,Order,BookInOrder
from main.models import book
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
    form = form_adress()

    if request.method == 'POST':
        form = form_adress(request.POST)
        cart = the_cart.objects.filter(customer = request.user)
        context = {
            'form':form,
            }
        if form.is_valid():
            #order = form.save(commit = False)
            #order.customer = request.user
            #order.save()
            if(len(cart)>0):
                order = Order.objects.create(customer=request.user)

                for cart in cart:
                    product = book.objects.get(pk=cart.title_book.pk)
                    quantity = cart.quentity
                    BookInOrder.objects.create(order=order, book=cart.title_book, quantity=quantity)


                messages.success(request, 'Order accepted')

            return render(request,'Order.html', context = context) 

            
    context = {
     'form':form,
    }
    return render(request,'cart/place_order.html', context = context)

def search(request):
    query_search = request.GET.get('search', '')
    if query_search:
        ad = book.objects.filter(title__icontains = query_search)
    else:
        ad = book.objects.all()
    context ={
        'ad':ad,
        }
    return render(request,'main/index.html',context = context)

def order(request):
    orders =  Order.objects.filter(customer = request.user)
    books = BookInOrder.objects.all()
    context = {
        'orders':orders,
        'books':books
        }
    return render(request,'Order.html',context = context)


