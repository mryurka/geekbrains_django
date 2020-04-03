from django.contrib import admin
from mainapp.models import ProductCategory
from mainapp.models import Product

# Register your models here.

admin.site.register(ProductCategory)
#admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'hot')
    list_filter = ('hot', 'category')
    search_fields = ('name', )
    # readonly_fields = 'quantity',
    # fields = 'name', 'price', 'category', - поля внутри




