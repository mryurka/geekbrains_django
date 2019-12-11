from django.shortcuts import render
from django.urls import resolve

# Create your views here.


def main(request):
    context = {
        'title': 'главная страница'
    }
    return render(request, 'mainapp/main.html', context)


def products(request, **kwargs):
    prod_cat = kwargs['product_category']

    links_menu = [
        {'href': 'products', 'product_category': 'all', 'name': 'все'},
        {'href': 'products', 'product_category': 'home', 'name': 'дом'},
        {'href': 'products', 'product_category': 'office', 'name': 'офис'},
        {'href': 'products', 'product_category': 'electronics', 'name': 'электроника'},
    ]

    all_products = {'home': [[3, 'стул', 2000, 'img/стул_79.jpg'],
                             [4, 'стол', 10000, 'img/стол_79.jpg'],
                             [5, 'таз', 150, 'img/таз_79.jpg']],
                    'office': [[6, 'Офисное кресло', 100, 'img/офисное_кресло_79.jpg'],
                               [7, 'Степлер', 300, 'img/степлер_79.jpg'],
                               [8, 'Скрепки', 250, 'img/скрепки_79.jpg']],
                    'electronics': [[9, 'телек', 10000, 'img/Xiaomi-TV_small.jpg'],
                                    [10, 'мобилофон', 20000, 'img/smartphone_small.jpg'],
                                    [11, 'робосос', 15000, 'img/robosos_small.jpg']]

                    }

    product_list = []
    if prod_cat != 'all':
        product_list = all_products[prod_cat]
    else:
        for keys in all_products:
            product_list += [item for item in all_products[keys]]

    context = {
        'title': 'наши продукты',
        'links_menu': links_menu,
        'prod_cat': prod_cat,
        'product_list': product_list,
    }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {
        'title': 'наши контакты'
    }
    return render(request, 'mainapp/contacts.html', context)


