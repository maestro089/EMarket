from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('moderator/', include('moderator.urls')),
    path('account/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('news/', include('news.urls')),

    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)