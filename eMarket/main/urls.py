from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile_user, name='profile'),
    path('store', views.index, name='store'),
    path('ad/<int:ad_id>', views.ad_info, name='ad_info'),
    path('contact', views.contact, name='contact'),
    path('edit_profile/<int:pk>', views.edit_profile.as_view(), name='edit_profile'),

]
