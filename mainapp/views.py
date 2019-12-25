from django.shortcuts import render
# from django.urls import resolve
from mainapp.models import ProductCategory
from mainapp.models import Product
from basket.models import BasketSlot
from basket.views import basket as basket_view
# from django.shortcuts import get_object_or_404

# Create your views here.


def main(request):
    context = {
        'title': 'главная страница'
    }
    return render(request, 'mainapp/main.html', context)


def products(request, category_pk=0):
    basket = {'basket': None, 'total_cost': 0}

    product_categories = ProductCategory.objects.all()

    if category_pk == 0:
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(category=category_pk)

    if request.user.is_authenticated:
        # print(request.user.basket.all())
        basket = basket_view(request)

    context = {
        'title': 'наши продукты',
        'prod_cats': product_categories,
        'basket': basket['basket'],
        'total_cost': basket['total_cost'],
        'product_list': product_list,
    }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {
        'title': 'наши контакты'
    }
    return render(request, 'mainapp/contacts.html', context)


