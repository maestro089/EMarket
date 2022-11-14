from django.urls import path, include
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile_user, name='profile'),
    path('store', views.index, name='store'),
    path('ad/<int:ad_id>', views.ad_info, name='ad_info'),
]
