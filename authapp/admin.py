from django.contrib import admin
from authapp.models import ShopUser
from basket.models import BasketSlot

# Register your models here.
admin.site.register(ShopUser)


# @admin.register(ShopUser)
# class JustShopUser(admin.ModelAdmin):
#     readonly_fields = ('password',)


class UserWithBasket(ShopUser):
    class Meta:
        verbose_name = 'Пользователь с корзиной'
        verbose_name_plural = 'Пользователи с корзиной'
        proxy = True


class BasketInLine(admin.TabularInline):
    model = BasketSlot
    extra = 0  # добавление пустых строк для заполнения


@admin.register(UserWithBasket)
class UserWithBasket(admin.ModelAdmin):
    list_display = 'username', 'get_basket_quantity', 'get_basket_cost',
    fields = 'username',
    readonly_fields = 'username',
    inlines = BasketInLine,

    def get_queryset(self, request):
        return ShopUser.objects.filter(basket__quantity__gt=0).distinct()

    def get_basket_quantity(self, instance):
        print(type(self))
        print(type(instance))
        return sum(list(map(lambda basket_slot: basket_slot.quantity, instance.basket.all())))

    def get_basket_cost(self, instance):
        return sum(list(map(lambda basket_slot: basket_slot.cost, instance.basket.all())))

    get_basket_cost.short_description = 'На сумму'
    get_basket_quantity.short_description = 'Товаров в корзине'

