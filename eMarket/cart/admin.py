from django.contrib import admin
from cart.models import the_cart, user_adress,Order, BookInOrder


admin.site.register(the_cart)
admin.site.register(user_adress)


class ProductsInOrderInline(admin.TabularInline):
    model = BookInOrder

    verbose_name = 'Order'
    verbose_name_plural = 'Orders'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('created',)
    list_display = ('customer', 'quantity', 'created', )

    inlines = (ProductsInOrderInline,)

    def quantity(self, obj):
        return BookInOrder.objects.filter(order=obj).count()

    quantity.short_description = 'Quantity order'


