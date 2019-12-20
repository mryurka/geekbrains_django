# from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from mainapp.models import Product
from .models import BasketSlot
# Create your views here.


#  def basket(request, product_pk):
#      pass


def basket_slot_add(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    slot = BasketSlot.objects.filter(user=request.user, product=product).first()
    if slot:
        slot.quantity += 1
        slot.save()
    else:
        slot = BasketSlot(user=request.user, product=product, quantity=1)
        slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_slot_remove(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    slot = BasketSlot.objects.filter(user=request.user, product=product).first()
    if slot:
        if slot.quantity > 1:
            slot.quantity -= 1
            slot.save()
        else:
            slot.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

