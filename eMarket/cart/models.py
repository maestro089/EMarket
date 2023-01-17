from django.db import models
from main.models import book
from django.contrib.auth.models import User


class the_cart(models.Model):
    object = None
    title_book = models.ForeignKey(book, on_delete=models.CASCADE, verbose_name='title book')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='customer')
    quentity = models.FloatField(verbose_name = "Quantity", null = True)

class user_adress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Customer')
    postal_code = models.FloatField(verbose_name = "Postal code")
    country = models.CharField(max_length=255, verbose_name = "Country")
    sity = models.CharField(max_length=255, verbose_name = "Sity")
    street = models.CharField(max_length=255, verbose_name = "Street")
    num_home = models.CharField(max_length=255, verbose_name = "Number home")

class Order(models.Model):
    STATUS_CHOICES = (
        ('processed', 'Обрабатывается'), 
        ('sent', 'Отправлен'), 
        ('delivered', 'Доставлен'), 
    )
    customer = models.ForeignKey(User, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Customer')
    books = models.ManyToManyField(book, verbose_name='Books', blank=True, through='BookInOrder')
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES, 
                              default='processed', verbose_name="Статус" )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Create date')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.books} - {self.created}'

    
class BookInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    book = models.ForeignKey(book, on_delete=models.PROTECT, verbose_name='Book', related_name='count_in_order',)
    quantity = models.PositiveSmallIntegerField(verbose_name='Quantity book')

    def __str__(self):
        return f'{self.book}'




