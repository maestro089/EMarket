from django.urls import path
from . import views 


urlpatterns = [
path('', views.index, name='news'),
path('<int:pk>', views.news_info, name='news_info'),
]
