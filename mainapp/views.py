from django.shortcuts import render
# from django.urls import resolve
from mainapp.models import ProductCategory
from mainapp.models import Product
from basket.models import BasketSlot
# from django.shortcuts import get_object_or_404

# Create your views here.


def main(request):
    context = {
        'title': 'главная страница'
    }
    return render(request, 'mainapp/main.html', context)


def products(request, category_pk=0):
    basket = None
    total_cost = 0

    product_categories = ProductCategory.objects.all()

    if category_pk == 0:
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(category=category_pk)

    if request.user.is_authenticated:
        whole_basket = BasketSlot.objects.filter(user=request.user)
        if whole_basket and len(whole_basket) > 0:
            basket = whole_basket
            for slot in whole_basket:
                total_cost += slot.get_cost()

    context = {
        'title': 'наши продукты',
        'prod_cats': product_categories,
        'basket': basket,
        'total_cost': total_cost,
        'product_list': product_list,
    }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {
        'title': 'наши контакты'
    }
    return render(request, 'mainapp/contacts.html', context)


