from django.contrib import admin
from .models import comment, news


admin.site.register(news)
admin.site.register(comment)

