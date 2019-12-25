from django.urls import path
import basket.views as basket_view

app_name = 'basket'

urlpatterns = [
    # path('', basket_view.basket, name='basket'),
    path('add/<int:product_pk>/', basket_view.basket_slot_add, name='add'),
    path('remove/<int:product_pk>/', basket_view.basket_slot_remove, name='remove'),
    path('edit/<int:slot_pk>/', basket_view.basket_slot_edit, name='edit'),
    ]

