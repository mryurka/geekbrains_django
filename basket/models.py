from django.db import models
from mainapp.models import Product
from django.conf import settings

# Create your models here.


class BasketSlot(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='время')

    @property
    def cost(self):
        cost = self.quantity * self.product.price
        return cost

    @property
    def product_name(self):
        return self.product.name

    def __str__(self):
        return f'{self.user} {self.product} {self.quantity} {self.product.price}'

