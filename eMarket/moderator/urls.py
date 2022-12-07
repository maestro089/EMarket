from django.urls import path, include
from . import views 


app_name = "moderator"

urlpatterns = [
    path('', views.moderator_main, name='moderator_main'),
    path('moderator_news/', views.moderator_news, name='moderator_news'),
    path('moderator_book/', views.moderator_book, name='moderator_book'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('add_menejer/<int:pk>', views.add_menejer, name='add_menejer'),
    path('edit_book/<int:pk>', views.edit_book.as_view(), name='edit_book'),
    path('create_book/', views.create_book.as_view(), name='create_book'),
    path('delete_book/<int:pk>', views.delete_book, name='delete_book'),


    path('edit_news/<int:pk>', views.edit_news.as_view(), name='edit_news'),
    path('create_news/', views.create_news.as_view(), name='create_news'),
    path('delete_news/<int:pk>', views.delete_news, name='delete_news'),
    path('delete_menejer/<int:pk>', views.delete_menejer, name='delete_menejer'),

    path('manager', views.manager_main, name='manager_main'),
]
