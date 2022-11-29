from django.urls import path, include
from . import views 


app_name = "moderator"

urlpatterns = [
    path('', views.moderator_main, name='moderator_main'),
    path('moderator_book/', views.moderator_book, name='moderator_book'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('add_menejer/', views.add_menejer, name='add_menejer'),
    path('delete_menejer/', views.delete_menejer, name='delete_menejer'),
]
