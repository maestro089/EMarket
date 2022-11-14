from django.db import models
from django.contrib.auth.models import User



class genre_of_the_book (models.Model):
    object = None
    title = models.CharField(max_length=255, blank = True, verbose_name="Title category")

    def __str__(self):
        return self.title


class Author_of_the_book(models.Model):
    objects = None
    name = models.CharField(max_length=255, verbose_name = "Name of the author")
    photo = models.ImageField(upload_to="photo/author/%Y/%m/%d/", verbose_name = "Book photo")
    description = models.TextField(blank=True, verbose_name = "Book description")

    def __str__(self):
        return self.name


class book (models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name = "Book name")
    isbn = models.CharField(null = True, blank = True, max_length=255, verbose_name = "isbn")
    photo = models.ImageField(upload_to="photo/book/%Y/%m/%d/", verbose_name = "Book photo")
    description = models.TextField(blank=True, verbose_name = "Book description")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = "Date of offering for sale")
    is_published = models.BooleanField(default=True, verbose_name = "Publisher")
    price = models.FloatField(verbose_name = "Price")
    Author = models.ForeignKey(Author_of_the_book, null = True, blank = True, verbose_name = "Author",on_delete = models.CASCADE)
    genre = models.ForeignKey(genre_of_the_book, null = False, blank = True, verbose_name = "Genre of the book",on_delete = models.CASCADE)


    def __str__(self):
        return self.title

class profile (models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    moderator = models.BooleanField(default=False, verbose_name = "moderator")


