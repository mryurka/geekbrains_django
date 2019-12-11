import os
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory
from mainapp.models import Product


class Command(BaseCommand):
    help = 'help would be cool... )'

    def handle(self, *args, **options):
        base_dir = settings.BASE_DIR
        sep = os.sep
        with open(os.path.join(base_dir, 'products.json'), encoding='utf-8') as input_json_file:
            data = json.load(input_json_file)
            print(data)
        for key in data:
            new_category = ProductCategory(name=key)
            try:
                new_category.save()
            except:
                new_category = ProductCategory.objects.get(name=key)
            products_list = data[key]
            for product in products_list:
                img = f'product_images{sep}{product[3]}' if product[3] else ""
                new_product = Product(name=product[0], price=product[1], quantity=product[2],
                                      image=img, category=new_category)
                new_product.save()

        return "DB processing done"


