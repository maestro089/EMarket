from django.db import models
from django.contrib.auth.models import User

class news (models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name = "News name")
    photo = models.ImageField(upload_to="photo/book/%Y/%m/%d/", verbose_name = "News photo")
    text = models.TextField(blank=True, verbose_name = "Text")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = "Date publisher")
    is_published = models.BooleanField(default=True, verbose_name = "Publisher")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

class comment(models.Model):
        object = None
        text = models.TextField(blank=True, verbose_name = "Text")
        author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
        news = models.ForeignKey(news, on_delete=models.CASCADE, verbose_name='news')

