# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from mainapp.models import Product
from .models import BasketSlot
from django.urls import reverse
# Create your views here.


@login_required
def basket(request):
    basket_set = None
    total_cost = 0
    whole_basket = request.user.basket.all()
    if whole_basket and len(whole_basket) > 0:
        basket_set = whole_basket
        for slot in whole_basket:
            total_cost += slot.cost
    return {'basket': basket_set, 'total_cost': total_cost}


@login_required
def basket_slot_add(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    slot = BasketSlot.objects.filter(user=request.user, product=product).first()
    if slot:
        slot.quantity += 1
        slot.save()
    else:
        slot = BasketSlot(user=request.user, product=product, quantity=1)
        slot.save()

        print(request.META.get('HTTP_REFERER'))

    if request.META.get('HTTP_REFERER') and request.META.get('HTTP_REFERER').find('login') > 0:
        response_target = reverse('mainapp:products', args=[product.category_id])
        print(response_target)
    else:
        response_target = request.META.get('HTTP_REFERER')

    return HttpResponseRedirect(response_target)


@login_required
def basket_slot_remove(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    slot = BasketSlot.objects.filter(user=request.user, product=product).first()
    if slot:
        if slot.quantity > 1:
            slot.quantity -= 1
            slot.save()
        else:
            slot.delete()

    if request.META.get('HTTP_REFERER') and request.META.get('HTTP_REFERER').find('login') > 0:
        response_target = reverse(reverse('mainapp:products', args=[product.category_id]))
    else:
        response_target = request.META.get('HTTP_REFERER')

    return HttpResponseRedirect(response_target)


def basket_slot_edit(request, slot_pk):
    # print(slot_pk)
    # print(request.GET.get('quantity'))
    slot = get_object_or_404(BasketSlot, pk=slot_pk)
    quantity = int(request.GET.get('quantity'))
    if quantity > 0:
        slot.quantity = quantity
        slot.save()
    else:
        slot.delete()

    return HttpResponse(f'status: ok, product_pk: {slot_pk}, quantity: {quantity}')


