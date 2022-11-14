from django.contrib import admin
from .models import Author_of_the_book, book, genre_of_the_book,profile


admin.site.register(book)
admin.site.register(profile)
admin.site.register(Author_of_the_book)
admin.site.register(genre_of_the_book)
