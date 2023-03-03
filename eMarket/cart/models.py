from django.db import models
from main.models import book
from django.contrib.auth.models import User


class the_cart(models.Model):
    object = None
    title_book = models.ForeignKey(book, on_delete=models.CASCADE, verbose_name='Книга')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель')
    quentity = models.IntegerField(verbose_name = "Количество", null = True)

class points_of_issue_adress(models.Model):
    country = models.CharField(max_length=255, verbose_name = "Страна")
    sity = models.CharField(max_length=255, verbose_name = "Город")
    street = models.CharField(max_length=255, verbose_name = "Улица")
    num_home = models.CharField(max_length=255, verbose_name = "Номер дома")

    def __str__(self):
        return f'{self.sity}, {self.street}, {self.num_home}'

class Order(models.Model):
    STATUS_CHOICES = (
        ('processed', 'Обрабатывается'), 
        ('sent', 'Отправлен'), 
        ('delivered', 'Доставлен'), 
    )
    customer = models.ForeignKey(User, related_name='Покупатель',
                                 on_delete=models.CASCADE, verbose_name='Покупатель')
    books = models.ManyToManyField(book, verbose_name='Книги', blank=True, through='BookInOrder')
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES, 
                              default='processed', verbose_name="Статус" )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    adress = models.ForeignKey(points_of_issue_adress, on_delete=models.PROTECT, verbose_name='Адресс доставки',null = True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.books} - {self.created}'

    
class BookInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    book = models.ForeignKey(book, on_delete=models.PROTECT, verbose_name='книга')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество книг')

    def __str__(self):
        return f'{self.book}'




