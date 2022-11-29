﻿from django.db import models
from django.contrib.auth.models import User



class genre_of_the_book (models.Model):
    object = None
    title = models.CharField(max_length=255, blank = True, verbose_name="Название категории")

    def __str__(self):
        return self.title


class Author_of_the_book(models.Model):
    objects = None
    name = models.CharField(max_length=255, verbose_name = "Имя автора")
    photo = models.ImageField(upload_to="photo/author/%Y/%m/%d/", verbose_name = "Фотография автора")
    description = models.TextField(blank=True, verbose_name = "Описание книги")

    def __str__(self):
        return self.name


class book (models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name = "Названеи книги")
    isbn = models.CharField(null = True, blank = True, max_length=255, verbose_name = "isbn")
    photo = models.ImageField(upload_to="photo/book/%Y/%m/%d/", verbose_name = "Фотография книги")
    description = models.TextField(blank=True, verbose_name = "Описание книги")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = "Дата публикации книги")
    is_published = models.BooleanField(default=True, verbose_name = "Публикация")
    price = models.FloatField(verbose_name = "Цена")
    Author = models.ForeignKey(Author_of_the_book, null = True, blank = True, verbose_name = "Автор",on_delete = models.CASCADE)
    genre = models.ForeignKey(genre_of_the_book, null = False, blank = True, verbose_name = "Кагория книги",on_delete = models.CASCADE)


    def __str__(self):
        return self.title

class profile (models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    moderator = models.BooleanField(default=False, verbose_name = "Администратор")
    photo = models.ImageField(upload_to="photo/user/%Y/%m/%d/", null = True, verbose_name = "Фото пользователя")

class comment_book(models.Model):
        object = None
        text = models.TextField(blank=True, verbose_name = "Текст комментария")
        author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
        book_in_comment = models.ForeignKey(book, on_delete=models.CASCADE, verbose_name='Книга')


