from django.urls import path
from . import views 


app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add_cart/', views.add_cart, name='add_cart'),
    path('order/', views.order, name='order'),
    path('filter_book/', views.filter_book, name='filter_book'),
    path('search/', views.search, name='search'),
    path('delete_cart/', views.delete_cart, name='delete_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('making_order/', views.making_order, name='making_order'),
] 


