from django.urls import path
from . import views 


app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add_cart', views.add_cart, name='add_cart'),
    path('order', views.order, name='order'),
    path('search', views.search, name='search'),
    path('delete_cart', views.delete_cart, name='delete_cart'),
    path('place_order', views.place_order, name='place_order'),
] 


