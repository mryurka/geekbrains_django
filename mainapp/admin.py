from django.contrib import admin
from mainapp.models import ProductCategory
from mainapp.models import Product

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
