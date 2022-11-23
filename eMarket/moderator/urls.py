from django.urls import path, include
from . import views 

app_name = "moderator"


urlpatterns = [
    path('', views.moderator_main, name='moderator_main'),

    
]
